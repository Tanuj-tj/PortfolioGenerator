from django import shortcuts
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/', default="profiles/user_profile.png")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkdin = models.CharField(max_length=200, blank=True, null=True)
    social_medium = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    # Override the id attribure
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)