from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails, VideosDetails


class UserDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserDetails
        fields = ('name','phone','email', 'password')


class VideosDetailsForm(forms.ModelForm):
    class Meta:
        model =VideosDetails
        fields = ('image','titleImage','thumbnailImage', 'title','description', 'year', 'genre', 'type', 'trailer', 'video')


class Video_form(forms.ModelForm):
    class Meta:
        model=VideosDetails
        fields=('image','titleImage','thumbnailImage', 'title','description', 'year', 'genre', 'type', 'trailer', 'video')