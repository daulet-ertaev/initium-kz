from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField()
    lastName = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email',  'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName = forms.CharField(required=False)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    payPalID = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['image','phoneNumber','classification','country', 'city']