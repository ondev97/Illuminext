from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Welcome

# Create your views here.

def home(request):
    return render(request,template_name='main/index.html',context={
        "welcome":Welcome.objects.filter().first()
    })


def about (request):
    return render(request,template_name='main/about.html')

def news(request):
    return render(request,template_name='main/news.html')

def contacts(request):
    return render(request,template_name='main/contact.html')

def services(request):
    return render(request,template_name='main/services.html')

def contactform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        organization = request.POST['org']
        phonenumber = request.POST['phonenumber']
        message = request.POST['message']
        checkbox_one = request.POST['one']
        #print(checkbox_one,name,email,organization,phonenumber,message)
    return HttpResponseRedirect('/contact')

