from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),
    path('contact/',views.contacts,name='contact'),
    path('services/',views.services,name='services'),
]
