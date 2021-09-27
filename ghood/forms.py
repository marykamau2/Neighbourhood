from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood, Profile, Post, Business


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')


# class NeighbourHoodForm(forms.ModelForm):
#     class Meta:
#         model = Neighbourhood
#         exclude = ('admin',)


# class BusinessForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         exclude = ('user', 'neighbourhood')


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ('user', 'hood')