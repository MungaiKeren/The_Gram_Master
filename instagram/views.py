from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    title = 'instagram-clone'
    param = {
        "title": title
    }
    return render(request, 'index.html', param)


def registration(request):
    form = UserCreationForm()
    param = {
        "form": form,
    }
    return render(request, 'registration/sign-up.html', param)
