from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile
from profiles import models


class UserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password',]


COURSE_CHOICES = [
        ('', 'Select a course'),  # Empty choice for default
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image', 'phone_number', 'email', 'city', 'dob', 'gender', 'course']
        widgets = {
            'phone_number': widgets.TextInput(attrs={
                'required': 'required',  # Mark as required
            }),
            'course': widgets.Select(choices=COURSE_CHOICES, attrs={
                'class': 'form-control',
                'required': 'required',  # Mark as required
            }),
            'image': widgets.FileInput(attrs={
                'class': 'fa fa-camera',
            }),
            'dob': widgets.DateInput(attrs={
                'type': 'date',
                'required': 'required',  # Mark as required
            }),
        }