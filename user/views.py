from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

# Create your views here.

@never_cache
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'user': request.user})
    else:
        return redirect('login')

@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'user/login.html')

def register(request):
     if request.user.is_authenticated:
        return redirect('index')
    
     if request.method == "POST":
        print(request.POST,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')

     return render(request, 'user/register.html')


def example(request):
    return render(request, 'user/example.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')