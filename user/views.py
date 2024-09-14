from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
import re

# Create your views here.


def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('/user/signin')

            # Get the user's profile
            user_profile = get_object_or_404(UserProfile, user=request.user)

            # Check if the user's role matches the required role
            if user_profile.role == role:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden(f"Access Denied: You do not have permission to view this page. This section is restricted to {role} only")
        return _wrapped_view
    return decorator





def user_dashboard(request):
    profiles = UserProfile.objects.all()

    return render(request, 'user_dashboard.html', {'profiles': profiles})


def user_view(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'user_view.html', {'profile': profile})


def user_edit(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':

        profile.phone = request.POST.get('phone')
        profile.city = request.POST.get('city')
        profile.address = request.POST.get('address')
        profile.save()

        return redirect('user_dashboard')

    return render(request, 'user_edit.html', {'profile': profile})


def user_delete(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)

    if request.method == 'POST':
        user = profile.user

        profile.delete()
        user.delete()
    return redirect('user_dashboard')








@role_required('Admin')
def home(request):
    return HttpResponse("Hello, " + request.user.username)

def is_username_valid(username):
    username_pattern = re.compile(r'^[a-zA-Z0-9._-]+$')
    if username_pattern.match(username):
        return True
    return False

def is_email_valid(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    if email_pattern.match(email):
        return True
    return False

def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            role = request.POST['role']


            if not is_username_valid(username):
                messages.info(request, 'Invalid username!')
                return redirect('/user/signup')


            if not is_email_valid(email):
                messages.info(request, 'Invalid email address!')
                return redirect('/user/signup')

            if password == confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('/user/signup')

                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('/user/signup')
                else:

                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    user_model = User.objects.get(username=username)

                    new_profile = UserProfile.objects.create(user=user_model,email=email, role=role, phone = phone)
                    new_profile.save()

                    return redirect('/')


            else:
                messages.info(request, 'Password Not Matching')
                return redirect('/user/signup')

        except Exception as e:
            messages.info(request, 'Something went wrong. Please try again')
            return redirect('/user/signin')


    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('/user/signin')

        except Exception as e:
            messages.info(request, 'Something went wrong. Please try again')
            return redirect('/user/signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('/user/signin')