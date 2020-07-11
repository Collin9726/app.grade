from PIL import Image
import tempfile
from django.test import TestCase
from django.test import override_settings
from .models import Profile, Project, Rating
from django.contrib.auth.models import User

# Create your tests here.
def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file


class ProfileTestClass(TestCase):
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # Set up method
    def setUp(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)            
        self.this_user =User.objects.create_user('mimi', 'mimi@gmail.com', 'moringa')        
        self.this_profile = Profile(bio='bio', account_holder= self.this_user, profile_photo = test_image.name)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_profile,Profile))

    # Testing Save Method
    def test_save_profile_method(self):
        self.this_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing Delete Method
    def test_delete_profile_method(self):
        self.this_profile.save_profile()
        profile = Profile.objects.get(bio ='bio')
        profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    # Testing Update Method
    def test_update_profile_method(self):        
        self.this_profile.save_profile()
        profile = Profile.objects.get(account_holder = self.this_user)        
        profile.bio = 'otherBio'
        profile.update_profile()
        query_set = Profile.objects.all()[:1]
        updated_profile=None
        for prof in query_set:
            updated_profile = prof
        self.assertEqual(updated_profile.bio, 'otherBio')



class ProjectTestClass(TestCase):
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # Set up method
    def setUp(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)            
        self.this_user =User.objects.create_user('mimi', 'mimi@gmail.com', 'moringa')        
        self.this_profile = Profile(bio='bio', account_holder= self.this_user, profile_photo = test_image.name)        
        self.this_profile.save_profile()
        self.this_project= Project(title='myproject', description='mydescription', link='https//:myproject.com', profile = self.this_profile, cover_image = test_image.name )

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.this_project,Project))


    # Testing Save Method
    def test_save_project_method(self):
        self.this_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    # Testing Delete Method
    def test_delete_project_method(self):
        self.this_project.save_project()
        project = Project.objects.get(title ='myproject')
        project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)