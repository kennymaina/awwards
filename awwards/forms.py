from django import forms
from .models import *




class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_photo', 'description','url','github_repo','owner','project_name')
