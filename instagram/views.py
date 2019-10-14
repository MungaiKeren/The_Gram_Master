from django.contrib import messages
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
    comment = Comment.get_all_comments()
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
        u_form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
    return render(request, 'edit_profile.html', {"u_form": u_form, "p_form": p_form})
