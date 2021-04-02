from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


def register(request):
    rform = RegisterForm()
    pform = ProfileForm()
    if request.method == "POST":
        rform = RegisterForm(request.POST)
        pform = ProfileForm(request.POST)
        try:
            a = User.objects.get_by_natural_key(
                username=request.POST.get('username'))
        except User.DoesNotExist:
            if rform.is_valid() and pform.is_valid():
                rform.save()
                a = User.objects.get_by_natural_key(
                    username=request.POST.get('username'))
                print(a)
                porf = Profile.objects.get(user=a)
                porf.branch = request.POST.get('phone')
                porf.save()
                return redirect('login')
            else:
                messages.error(request, "Enter Details correctly")
                return redirect('register')
        messages.error(request, "User with this user name already exists!!")
        return redirect('register')
    return render(request, 'accounts/register.html', {'rform': rform, 'pform': pform})


@login_required()
def logout_user(request):
    logout(request)
    return redirect('login')


def login_user(request):
    form = AuthForm()
    if request.method == "POST":
        email = request.POST.get('email_id')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email.lower()).username
        except User.DoesNotExist:
            messages.error(request, "User Not found !")
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User Not found !")
            return redirect('login')
    return render(request, "accounts/login.html", {'form': form})
