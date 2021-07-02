from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    age = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    profession = models.CharField(max_length=200,null=True,blank=True)
    organization = models.CharField(max_length=200,null=True,blank=True)
    ctag = models.CharField(max_length=200,null=True,blank=True)
    portfolio = models.CharField(max_length=200,null=True,blank=True)
    github = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    tag = models.CharField(max_length=200,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created = models.CharField(max_length=200,null=True,blank=True)
    completed = models.CharField(max_length=200,null=True,blank=True)
    achievements = models.TextField(max_length=200,null=True,blank=True)
    tech = models.CharField(max_length=200,null=True,blank=True)
    github = models.CharField(max_length=200,null=True,blank=True)
    live = models.CharField(max_length=200,null=True,blank=True)
    opf1 = models.CharField(max_length=200,null=True,blank=True)
    opfl1 = models.CharField(max_length=200,null=True,blank=True)
    opf2 = models.CharField(max_length=200,null=True,blank=True)
    opfl2 = models.CharField(max_length=200,null=True,blank=True)
    opf3 = models.CharField(max_length=200,null=True,blank=True)
    opfl3 = models.CharField(max_length=200,null=True,blank=True)
    opf4 = models.CharField(max_length=200,null=True,blank=True)
    opfl4 = models.CharField(max_length=200,null=True,blank=True)
    imgl = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title


