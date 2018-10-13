from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=128)
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)
    captcha = CaptchaField(label='verification code')

class RegisterForm(forms.Form):
    gender = (
        ('male', "male"),
        ('female', "female"),
    )
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="check the password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='gender', choices=gender)
    captcha = CaptchaField(label='verification code')