from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('order')
        else:
            messages.success(request, 'Invalid user')
            return render(request, 'login.html')
    else:
         return render(request, 'login.html')
     
def logout_user(request):
    logout(request)
    messages.success(request, 'User logged out ')
    return redirect('home')

def order_page(request):
    return render(request, 'order.html')

def contact(request):
    return render(request, 'contact.html')

def Register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('order')  # Redirect to the desired page after successful registration
        else:
            messages.error(request, 'Invalid data')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the user's session to prevent them from being logged out after changing their password
            update_session_auth_hash(request, user)
            return redirect('home')
        else:
            # Redirect to login page if user is not authenticated
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})