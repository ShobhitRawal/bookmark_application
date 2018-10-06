import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Again', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        #password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        raise forms.ValidationError('Passwords do not match')

    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get('username')
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Invalid Username')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken')
