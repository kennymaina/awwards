from django.test import TestCase
from .models import *


class ProjectsTestCase(TestCase):
    def setUp(self, 'project_photo= 'bgimage.jpg', 'description='project description','url='site url','github_repo ='git repo','owner='kennymaina','project_name='awwards'):
        return Projects.objects.create('project_photo', 'description','url','github_repo','owner','project_name')

    def projectSave(self):
        initialization = self.setUp()
        self.assertTrue(save > 0)