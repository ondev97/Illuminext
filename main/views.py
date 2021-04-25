from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,template_name='main/index.html')

def about (request):
    return render(request,template_name='main/about.html')

def news(request):
    return render(request,template_name='main/news.html')

def contacts(request):
    return render(request,template_name='main/contact.html')

def services(request):
    return render(request,template_name='main/services.html')