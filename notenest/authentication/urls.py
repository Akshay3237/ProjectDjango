# authentication/urls.py

from django.urls import path
from .views import register_user,login_user,home,otpVerification,profile_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('home/', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('otp/',otpVerification,name='otpVerification'),
    path('profile/', profile_view, name='profile'),
]
