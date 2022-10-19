from asyncio.windows_events import NULL
from email.mime import image
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    heading = models.CharField(max_length = 50,null=True)
    image = models.ImageField()
    caption = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self): 
        return f"{self.user} + {self.caption[:20]}"


# class Profile(models.Model):
#         user = models.ForeignKey(User,on_delete=models.CASCADE)
#         bio = models.CharField(max_length=50)
#         followers = models.IntegerField(default=0)
#         following = models.IntegerField(default=0)
#         image = models.ImageField()

#         def __str__(self):
#              return str(self.user)



