from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form": form})


@login_required(login_url='/login')
def index(request):
    title = 'instagram-clone'
    posts = Image.get_images()
    param = {
        "title": title,
        "posts": posts
    }
    return render(request, 'index.html', param)


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_data = form.save(commit=False)
            profile_data.user = current_user
            profile.save()
        return redirect('/profile')
    else:
        form = ProfileForm()
        params = {
            "form": form
        }
    return render(request, 'profile.html', params)


@login_required(login_url='/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {"form": form})

