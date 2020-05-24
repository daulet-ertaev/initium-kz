from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    phoneNumber = forms.CharField()
    profession = forms.CharField()

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email', 'phoneNumber', 'profession', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName = forms.CharField(required=False)
    email = forms.EmailField()
    phoneNumber = forms.CharField(required=False)
    profession = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email', 'phoneNumber', 'profession']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']