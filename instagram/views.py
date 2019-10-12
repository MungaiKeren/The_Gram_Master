from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


# Create your views here.
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
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
        params = {
            "form": form
        }
    return render(request, 'profile.html', params)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegisterForm()
    param = {
        "form": form,
    }
    return render(request, 'registration/sign-up.html', param)
