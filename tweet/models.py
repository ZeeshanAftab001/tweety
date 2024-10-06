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
    
class Tweet(models.Model):

    user=models.ForeignKey(User,related_name="tweets",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=200)

    creation_time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} created {self.body[0:30]} at {self.creation_time}"
