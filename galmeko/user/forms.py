from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name','last_name','email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email',)
