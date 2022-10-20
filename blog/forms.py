from django import forms
from .models import Comment
from django.contrib.auth.forms import UserChangeForm
from django.conf import settings
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
