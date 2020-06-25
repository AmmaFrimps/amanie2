from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Queries


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'phone_number', 'work_id', 'location', 'rank')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'phone_number', 'work_id', 'location', 'rank')


class QueryForm(forms.ModelForm):
    class Meta:
        model = Queries
        fields = ("query_email", "subject", "message")


class PasswordResetForm(forms.Form):
    new_password1 = forms.CharField(max_length=100)
    new_password2 = forms.CharField(max_length=100)
