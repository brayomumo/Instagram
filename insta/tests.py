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

class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.image = Image(image='imageurl', image_name='fashion', image_caption='cool denim', profile='cool', likes='45', pub_date='12-03-2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,image))

    #Testing the save method
    def test_save_method(self):
        self.image.save_image()
        image = image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_method(self):
        self.image.save_delete()
        self.image.delete_image()
        image = image.objects.all()
        self.assertTrue(len(image)==0)  
