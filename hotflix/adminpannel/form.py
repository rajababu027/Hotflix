from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails


class UserDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ('userId', 'name','phone','email', 'password')