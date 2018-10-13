from django.shortcuts import render
from django.shortcuts import redirect
import datetime
from django.conf import settings

# Create your views here.
from login import forms, models


def index(request):
    pass
    return render(request, 'index.html')

def register(request):
    pass
    return render(request, 'register.html')

def base(request):
    pass
    return render(request, 'base.html')

def login(request):
    pass
    return render(request, 'login.html')

def logout(request):
    pass
    return redirect("/index/")

def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "please check the contents!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "password is wrong!"
            except:
                message = "user doesn't exsist!"
        return render(request, 'login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login.html', locals())

def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "please check the content"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "password are different!"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'username has been used!'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'the address has been registed!'
                    return render(request, 'register.html', locals())


                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())


