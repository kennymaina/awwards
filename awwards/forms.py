from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_photo', 'description','url','owner','project_name')
