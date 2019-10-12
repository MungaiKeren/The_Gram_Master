from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import *


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
