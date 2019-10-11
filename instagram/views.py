from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm


# Create your views here.
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
        return redirect('/')
    else:
        form = RegisterForm()
    param = {
        "form": form,
    }
    return render(request, 'registration/sign-up.html', param)
