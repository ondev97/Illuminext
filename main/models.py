from django.db import models
import random
import string
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# home page models


class Welcome(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    subtitle = models.CharField(max_length=300,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)
    phone_no = models.CharField(max_length=15,null=True,blank=True)
    title2 = models.CharField(max_length=300,blank=True,null=True)
    title2_content= models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Welcome"



class Specialization(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title


class SpecializationItem(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    content = models.CharField(max_length=600,null=True,blank=True)
    icon = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.title


class ClientSection(models.Model):
    description = RichTextField(null=True,blank=True)
    client_name = models.CharField(max_length=300,null=True,blank=True)
    client_post = models.CharField(max_length=300,null=True,blank=True)
    client_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = "Client Section"


class OurRecentProjects(models.Model):
    title = models.CharField(max_length=600,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Our Recent Project"

class OurRecentProjectsItem(models.Model):
    caption = models.CharField(max_length=300,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.caption


class Team(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=500,null=True,blank=True)
    post = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    description2 = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


# about us section

class OurStory(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Our Stories"


class WhatWeOffer(models.Model):
    description = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "What We Offer"



def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))



class WhatWeOfferObjects(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(max_length=255,unique=True,null=True,blank=True)

    class Meta:
        verbose_name_plural = "What We Offer Object"


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug()+"-"+self.title)
        super(WhatWeOfferObjects,self).save(*args,**kwargs)


# Services Section

class Services_heading(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    description = models.CharField(max_length=600,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Service Heading"


class Services(models.Model):
    client_name = models.CharField(max_length=300,null=True,blank=True)
    project_name = models.CharField(max_length=300,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    image_description = RichTextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    client_image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = "Services"



class ContactInfo(models.Model):
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    email  = models.EmailField(null=True,blank=True)
    website_url = models.URLField(null=True,blank=True)
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    twitter_url = models.URLField(null=True,blank=True)
    description = models.CharField(null=True,blank=True,max_length=600)

    def __str__(self):
        return self.phone_no


    class Meta:
        verbose_name_plural = "Contact Info"
