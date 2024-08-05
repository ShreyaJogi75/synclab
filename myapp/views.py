from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def index9(request):
    return render(request, "index9.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def errorpage(request):
    return render(request, "404.html")    

def contact(request):
    return render(request, "contact.html")
    
def help(request):
    return render(request, "help.html")  

def projects(request):
    return render(request, "projects.html")