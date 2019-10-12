from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
    title = 'instagram-clone'
    param = {
        "title": title
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
