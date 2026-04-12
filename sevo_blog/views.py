from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "sevo_blog/index.html", {
        "title": "Welcome to Sevo's Blog",
    })
