from django import forms
from django.forms.widgets import Select
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox , ReCaptchaV2Invisible , ReCaptchaV3 
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(forms.Form):
    error_css_class = 'text-danger'
    required_css_class = 'required'

    user_name=forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your user name"})
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"})
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"})
    )
    password2=forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password again"})
    )
    captcha = ReCaptchaField(
            widget=ReCaptchaV2Checkbox
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError('This username has already been taken ')
        return user_name

    def clean_email(self) :
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists() :
            raise forms.ValidationError('This Email has already been taken ')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2 :
            raise forms.ValidationError('The passwords entered are not the same ')
        return data