from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from .models import (Welcome,
                     Specialization,
                     SpecializationItem,ClientSection,
                     OurRecentProjects, ContactInfo,
                     OurRecentProjectsItem,
                     Team, OurStory, Services,
                     WhatWeOffer, WhatWeOfferObjects)


# Create your views here.

def home(request):
    return render(request, template_name='main/index.html', context={
        "welcome": Welcome.objects.filter().first(),
        "specialization": Specialization.objects.filter().first(),
        "specItem": SpecializationItem.objects.all(),
        "projects": OurRecentProjects.objects.filter().first(),
        "projectItem": OurRecentProjectsItem.objects.all(),
        "team": Team.objects.filter().first(),
        "client1":ClientSection.objects.get(id=1),
        "client2":ClientSection.objects.get(id=2),
        "client3":ClientSection.objects.get(id=3),

    })


def about(request):
    return render(request, template_name='main/about.html', context={
        "ourstory": OurStory.objects.filter().first(),
        'recent': WhatWeOfferObjects.objects.all()[:3],
        'recent_heading': WhatWeOffer.objects.filter().first()
    })


def news(request):
    return render(request, template_name='main/news.html', context={
        "offer": WhatWeOffer.objects.filter().first(),
        "offerItems": WhatWeOfferObjects.objects.all()[:4]
    })


def newsmore(request, slug):
    return render(request, template_name='main/news-more.html', context={
        "post": WhatWeOfferObjects.objects.get(slug=slug),
        "recent": WhatWeOfferObjects.objects.all()[:3]
    })


def contacts(request):
    return render(request, template_name='main/contact.html', context={
        "contact": ContactInfo.objects.filter().first()
    })


def services(request):
    return render(request, template_name='main/services.html', context={
        "item1": Services.objects.get(id=1),
        "item2": Services.objects.get(id=2),
        "item3": Services.objects.get(id=3),
    })

def contactform(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        organization = request.POST['org']
        phonenumber = request.POST['phonenumber']
        message = request.POST['message']
        checkbox_one = request.POST['one']
        student = request.POST['two']
        women = request.POST['three']
        body = "name:- " + name + "\n" + message + "\n" + "Session Type" + checkbox_one,student,women
        send_mail("Message from Illuminext",body,)
    return HttpResponseRedirect('/contact')


