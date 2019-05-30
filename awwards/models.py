from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User



# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='projectpics/')
    description = models.TextField(max_length=600, blank=True)
    # github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
 
    def save_project(self):
        self.save()


    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.project_name

    @classmethod
    def get_by_id(cls, id):
        details = Project.objects.filter(owner=id)
        return details
    
    @classmethod
    def get_all_projects(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def search_by_project(cls, search_term):
        project = Project.objects.filter(project_name__icontains=search_term)
        return project


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null = True)
    full_name = models.CharField(max_length=255, null=True)
    project = models.ForeignKey(Project,null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user=id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user=id).first()
        return details

