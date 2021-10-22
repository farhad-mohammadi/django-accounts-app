from django import forms
from captcha.fields import ReCaptchaField
#from django.contrib.auth import get_user_model

class SignUpForm(forms.Form):
    user_name=forms.CharField(
        widget=forms.TextInput()
    )
    email=forms.EmailField(
        widget=forms.EmailInput()
    )
    password=forms.CharField(
        widget=forms.PasswordInput()
    )
    password2=forms.CharField(
        widget=forms.PasswordInput()
    )
    captcha = ReCaptchaField()
