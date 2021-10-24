from django.shortcuts import render

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

