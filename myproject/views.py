# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html.j2")
    # return HttpResponse("Hello World! I'm Home")


def about(request):
    return render(request, "about.html.j2")

    # return HttpResponse("My About page")
