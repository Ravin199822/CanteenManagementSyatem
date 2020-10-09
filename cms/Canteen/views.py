from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def home(request):
    return render(request,"home.html")

def showitems(request):
    return render(request,"showitems.html")

def payment(request):
    return render(request,"payment.html")

def successful(request):
    return render(request,"successful.html")