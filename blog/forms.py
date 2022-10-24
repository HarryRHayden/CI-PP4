from django import forms
from .models import Comment, Personal
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm


# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for user to input first and last name details
class EditUser(UserChangeForm):
    password = None
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"})
        }
