from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User



# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='projectpics/')
    description = models.TextField(max_length=600, blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.url
    
    @classmethod
    def search_by_project(cls, search_term):
        project = Project.objects.filter(title__icontains=search_term)
        return project


class Profile(models.Model):
    name = models.CharField(max_length =30)
# class Meta:
#         ordering = ['-pk']

    def save_profile(self):
        self.save()
