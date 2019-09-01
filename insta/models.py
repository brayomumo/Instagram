from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField('profile/', null = True)
    bio = models.TextField()
    user = models.ForeignKey(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-last_update']

    def __str__(self):
        return self.user.name

class Image(models.Model):
    image = models.ImageField(upload_to ='image/', null=True)
    image_name = models.CharField(max_length =30, null=True)
    image_caption = models.TextField(null=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    comment = models.CharField(null = True, max_length= 5000, verbose_name = 'name')
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True)
    image = models.ForeignKey(Image, null= True)
