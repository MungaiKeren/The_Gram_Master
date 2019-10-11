from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    title = 'instagram-clone'
    param = {
        "title": title
    }
    return render(request, 'index.html', param)

