from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home_page, name='Home_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/login/', views.login),
    path('flower_bouquet/', views.flower_bouquet,
         name='flower_bouquet'),
    path('logout/', views.logout, name='logout'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('buy/<int:id>', views.buy, name='buy'),

]
