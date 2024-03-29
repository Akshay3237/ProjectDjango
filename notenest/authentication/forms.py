from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Student, Tutor, Parent,User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    usertype = forms.ChoiceField(choices=User.USERTYPE_CHOICES)  # Add the usertype field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'usertype']  # Include usertype in the fields list


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'student_id']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        exclude = ['user', 'tutor_id']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ['user', 'parent_id']