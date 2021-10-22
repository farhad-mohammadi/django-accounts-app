from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from django.contrib.auth import authenticate, login, get_user_model
from .forms import SignUpForm

def home(request):
    return HttpResponse('home')

User=get_user_model()

def signup(request):
    form=SignUpForm(request.POST or None)
    print(form)
    context={
        'form':form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        user_name=form.cleaned_data.get('user_name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user=User.objects.create_user(username=user_name, email=email, password=password)
        redirect('home')
    return render(request, 'signup.html', context)