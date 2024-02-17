# authentication/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import random

def generate_random_4_digit():
    return random.randint(1000, 9999)
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            subject = "Verify Your Email Address"
            from_email = "multiwebsites4@gmail.com"
            to = request.POST['email']
            text_content = "This is an important message."
            otp=generate_random_4_digit()
            request.session['otpCode']=otp
            request.session['user']=form.cleaned_data
            # Render the HTML content from an HTML template file
            html_content = render_to_string('verification_mail.html', {'otp': otp,'user':request.POST['username']})

            # Create an EmailMultiAlternatives object
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

            # Attach the HTML content as an alternative
            msg.attach_alternative(html_content, "text/html")

            # Send the email
            msg.send()
            return render(request,'otppage.html')  # Redirect to otppage after sending mail
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegistrationForm

def otpVerification(request):
    otp = request.GET.get('otp')
    otp_code = request.session.get('otpCode')
    if str(otp) == str(otp_code):
        user_data = request.session.get('user')
        if user_data:
            form =UserRegistrationForm(user_data)
            if form.is_valid():
                form.save()
                return render(request,'login.html',{'success_message':'Account created successfully. You can now log in.'})
            else:
                return render(request,'login.html',{'success_message':'something'})
        else:
            return render(request,'register.html',{'error':'User data not found in session.','form':UserRegistrationForm()})
    else:
        return render(request,'register.html',{'error':'Invalid OTP. Please try again.','form':UserRegistrationForm()})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Change 'home' to your desired URL name
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
    


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')
