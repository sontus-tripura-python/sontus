from django.db import models
from django.urls import reverse
# Create your models here.
class MyInfo(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='myphoto')
    fb = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    email =models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Services(models.Model):
    ICON_CHOICES = (
        ('laptop', 'laptop'),
        ('photo', 'photo'),
        ('code', 'code'),
        ('film', 'film'),
        ('rocket', 'rocket'),
        ('paint-brush', 'paint-brush'),
        
    )
    title = models.CharField(max_length=200)
    icon = models.CharField(choices=ICON_CHOICES, max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    about_description = models.TextField(max_length=200)
    city = models.CharField(max_length=200)
    education_degree = models.CharField(max_length=200)
    birthday = models.CharField(max_length=30)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name } + {self.position}"

class EducationDetail(models.Model):
    session = models.CharField(max_length=50)
    degree_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.degree_name

class ExprienceDetail(models.Model):
    session = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    project_photo = models.ImageField(upload_to='portfolio')
    project_link = models.URLField()
    project_name = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, default="New", choices=(("New", "New"), ("Read", "Read"), ("Closed", "Closed")))
    sentTime =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact"


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title