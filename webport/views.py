from django.shortcuts import render

def home(request):
    return render(request, "home.html")  # Renders the home.html template

def cv(request):
    return render(request, "cv.html")  # Renders the cv.html template
