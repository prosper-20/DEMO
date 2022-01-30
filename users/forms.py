import email
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(help_text="Enter a valid email address")

    class meta:
        model = User

        fields=["username", "email", "password1", "password2"]

        