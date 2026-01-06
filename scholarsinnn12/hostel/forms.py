from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Student


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class StudentExtraForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Phone number must be 9-15 digits and may include a + prefix.'
    )

    phone = forms.CharField(
        max_length=15,
        validators=[phone_validator],
        required=True
    )

    parent_phone = forms.CharField(
        max_length=15,
        validators=[phone_validator],
        required=True
    )

    class Meta:
        model = Student
        fields = ['roll', 'phone', 'parent_phone']
