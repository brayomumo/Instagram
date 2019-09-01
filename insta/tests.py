from django.test import TestCase
from .models import Profile,Image,Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    #Set Up method
    def setUp(self):
        self.profile = Profile(profile_photo='yes we can', bio='very awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    #Testing save method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)
