from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import User
from django.contrib import messages
from .forms import UserRegistrationForm
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from academic_info.models import Branch

from quiz_system.models import Result
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
            otp = generate_random_4_digit()
            request.session['otpCode'] = otp
            request.session['user'] = form.cleaned_data
            # Render the HTML content from an HTML template file
            html_content = render_to_string('verification_mail.html', {'otp': otp, 'user': request.POST['username']})

            # Create an EmailMultiAlternatives object
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

            # Attach the HTML content as an alternative
            msg.attach_alternative(html_content, "text/html")

            # Send the email
            msg.send()
            return render(request, 'otppage.html')  # Redirect to otppage after sending mail
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def otpVerification(request):
    otp = request.GET.get('otp')
    otp_code = request.session.get('otpCode')
    if str(otp) == str(otp_code):
        user_data = request.session.get('user')
        if user_data:
            form = UserRegistrationForm(user_data)
            if form.is_valid():
                form.save()
                return render(request, 'login.html', {'success_message': 'Account created successfully. You can now log in.'})
            else:
                return render(request, 'login.html', {'success_message': 'something is wrong'})
        else:
            return render(request, 'otppage.html', {'error': 'User data not found in session.', 'form': UserRegistrationForm()})
    else:
        return render(request, 'otppage.html', {'error': 'Invalid OTP. Please try again.', 'form': UserRegistrationForm()})


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


def home(request):
    branches = Branch.objects.all()
    return render(request, 'home.html', {'branches': branches})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Avg
import json
from quiz_system.models import Result, Quiz

def profile_view(request):
    # Get the current user
    user = request.user
    # Retrieve the user's test results
    test_results = Result.objects.filter(user=user)
    # Calculate the average marks
    average_marks = test_results.aggregate(Avg('score'))['score__avg'] or 0
    # Retrieve the quiz data for the user
    quiz_data = {}
    for result in test_results:
        quiz = result.quiz
        quiz_key = str(quiz.quiz_id) # Use the quiz ID as the key
        if quiz_key not in quiz_data:
            quiz_data[quiz_key] = {'scores': [], 'labels': []}
        quiz_data[quiz_key]['scores'].append(result.score)
        quiz_data[quiz_key]['labels'].append(quiz.subject.subject_name)  # Assuming you have a 'name' attribute in your Subject model
    # Serialize quiz data to JSON
    quiz_data_json = json.dumps(quiz_data, cls=DjangoJSONEncoder)
    # Pass data to the template
    context = {
        'user': user,
        'test_results': test_results,
        'average_marks': average_marks,
        'quiz_data': quiz_data_json
    }
    return render(request, 'profile.html', context)


def about_us_view(request):
    
    return render(request,'about_us.html')

from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TutorForm, ParentForm
from .models import Student, Tutor, Parent

def user_info_form(request):
    user = request.user
    form = None
    instance = None

    # Determine the appropriate form class based on the user's type
    if user.usertype == 's':
        form_class = StudentForm
        model_class = Student
    elif user.usertype == 't':
        form_class = TutorForm
        model_class = Tutor
    elif user.usertype == 'p':
        form_class = ParentForm
        model_class = Parent
    
    try:
        # Check if there's an existing instance for the user
        instance = model_class.objects.get(user=user)
    except model_class.DoesNotExist:
        # If the instance doesn't exist, create a new one
        instance = model_class(user=user)  # Create a new instance with user set
    
    if request.method == 'POST':
        # If there's an existing instance, update its data; otherwise, create a new record
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to success page after saving
    else:
        # If there's an existing instance, initialize the form with its data
        form = form_class(instance=instance)

    return render(request, 'user_info_form.html', {'form': form})

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Avg
import json
from quiz_system.models import Result, Quiz

def show_result(request):
    if request.method == 'POST':
        student_id = request.POST.get('studentID')
        # Retrieve the test results for the student
        u=User.objects.all().filter(id=student_id)
        
        test_results = Result.objects.filter(user_id=student_id)
        
        
        # Calculate the average marks
        average_marks = test_results.aggregate(Avg('score'))['score__avg'] or 0
        # Retrieve additional data related to the tests
        quiz_data = {}
        for result in test_results:
            quiz = result.quiz
            quiz_key = str(quiz.quiz_id) # Use the quiz ID as the key
            if quiz_key not in quiz_data:
                quiz_data[quiz_key] = {'scores': [], 'labels': []}
            quiz_data[quiz_key]['scores'].append(result.score)
            quiz_data[quiz_key]['labels'].append(quiz.subject.subject_name)  # Assuming you have a 'name' attribute in your Subject model
        # Serialize quiz data to JSON
        quiz_data_json = json.dumps(quiz_data, cls=DjangoJSONEncoder)
        # Pass data to the template
        context = {
            'test_results': test_results,
            'average_marks': average_marks,
            'quiz_data': quiz_data_json,
            'student':u,
        }
        return render(request, 'result.html', context)
    else:
        # If the request method is not POST, return an error message
        return redirect('home')
