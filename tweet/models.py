from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    follows=models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    picture=models.ImageField(upload_to='images/',blank=True)
    bio=models.TextField(max_length=255,blank=True)

    def __str__(self):
        return self.user.username