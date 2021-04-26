from django.db import models

#home page models

class Welcome(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    subtitle = models.CharField(max_length=300,blank=True,null=True)
    image = models.ImageField()
    phone_no = models.IntegerField(null=True,blank=True)
    title2 = models.CharField(max_length=300,blank=True,null=True)
    title2_content= models.TextField

class Specialization(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    content = models.TextField

class Specialization_item(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    content = models.CharField(max_length=600,null=True,blank=True)

class Client_section(models.Model):
    pass


class Team(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=500,null=True,blank=True)
    post = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField
    description = models.TextField





























class Service(models.Model):
    title = models.CharField(max_length=500,null=True,blank=True)
    content = models.TextField


