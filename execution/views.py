from django.shortcuts import render, redirect
from . models import user_details, flower_product
from django.contrib import messages


# Create your views here.


def Home_page(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if user_details.objects.filter(email=email):
                messages.info(request, 'Please enter new email',
                              extra_tags='email')
                return redirect('signup')
            elif user_details.objects.filter(username=username):
                messages.info(request, 'Please enter new username',
                              extra_tags='username')
                return redirect('signup')
            else:
                strn = user_details(username=username,
                                    email=email, password=password)
                strn.save()
                return redirect('/')
        else:
            messages.info(request, 'Please Enter password properly',
                          extra_tags='password')
            return redirect('signup')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        if(user_details.objects.filter(username=request.POST['username'], password=request.POST['password'])):
            user = user_details.objects.get(
                username=request.POST['username'], password=request.POST['password'])
        messages.info(request, 'you have successfully logged in',
                      extra_tags='success')
        request.session['username'] = user.username
        return render(request, 'index.html', {'user': user})

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('/')
    return redirect('/')


def flower_bouquet(request):
    flt = flower_product.objects.all()
    return render(request, 'flower_bouquet.html', {'flt': flt})


def user_profile(request):
    return render(request, 'user_profile.html')


def buy(request, id):
    if request.session.get('username') == None:
        messages.info(request, 'Please Login First', extra_tags='unortho')
        return redirect('login')

    smg = flower_product.objects.get(id=id)

    return render(request, 'buy.html', {'smg': smg})
