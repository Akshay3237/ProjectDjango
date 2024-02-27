from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    usertype = forms.ChoiceField(choices=User.USERTYPE_CHOICES)  # Add the usertype field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'usertype']  # Include usertype in the fields list
