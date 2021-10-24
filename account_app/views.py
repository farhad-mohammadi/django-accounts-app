from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.contrib.auth import authenticate, login, get_user_model
from django import forms
from .forms import SignUpForm, LoginForm
User=get_user_model()

def home(request):
    if request.user.is_authenticated :
        user = request.user.username
    else:
        user = None
    context={
        'page_title': 'صفحه اصلی',
        'user' : user,
    }
    return render(request, 'home.html', context)

def signup_page(request):
    form=SignUpForm(request.POST or None)
    context={
        'page_title': 'ثبت نام',
        'form':form,
    }
    if form.is_valid():
        user_name=form.cleaned_data.get('user_name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user=User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/')
    return render(request, 'account_app/signup.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'page_title': 'ورود',
        "form": form
    }    
    if form.is_valid():
        user_name = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None :
            login(request, user)
            return redirect('/')
        else:
            context={
                'page_title': 'ورود',
                'form': form,
            }
            
    return render(request, "account_app/login.html", context)

