from django.contrib.auth.models import User
from django import forms
from .models import Posts, Topics, Sections


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class ModifyForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['body']


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['body']


class AddTopicForm(forms.ModelForm):

    class Meta:
        model = Topics
        fields = ['title']


class AddSectionForm(forms.ModelForm):

    class Meta:
        model = Sections
        fields = ['title', 'description']


class ModifyPassword(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']


class ModifyEmail(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']