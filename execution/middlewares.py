from django.shortcuts import redirect


def LoginRequireM(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        if request.session.get('username') == None:
            return redirect('buy')

        response = get_response(request)

        return response

    return middleware
