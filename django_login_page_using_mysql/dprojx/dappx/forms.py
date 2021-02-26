from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email','is_staff','is_superuser')

class userprofileinfoform(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']