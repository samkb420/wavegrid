from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=300, null=True, blank=True)
    completed = models.BooleanField(default=True)


    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-id',)    
        

class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images', blank=True, null=True) 

    def __str__ (self):
        return self.project.title


    class Meta:
        verbose_name_plural = 'ProjectImages'
        ordering = ('-id',)
          

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    testimony = models.TextField()
    image = models.ImageField(upload_to='images', default="", blank=True, null=True)


    def __str__ (self):
        return self.name    

    class Meta:
        verbose_name_plural= 'Feedbacks'
        ordering = ('-id',)       

class Contact(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300)
    message = models.TextField()

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ('-id',) 

class Partners(models.Model):
    image = models.FileField(upload_to='images', null=True, blank=True)          

   
