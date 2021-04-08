# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Project,Profile,Review
# # Create your tests here.


class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(first_name = 'James', last_name ='Muriuki', bio ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.project= Project(title = 'musical', description ='experience',)
        self.project2= Project(title = 'musical2', description ='experience2',)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects  = Project.objects.all()
        self.assertTrue(len(projects)>0)


