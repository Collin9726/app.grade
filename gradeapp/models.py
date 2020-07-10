from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(upload_to = 'profilepics/', blank=True)
    bio = models.TextField()
    account_holder = models.ForeignKey(User,on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.account_holder.username}'s profile" 

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()