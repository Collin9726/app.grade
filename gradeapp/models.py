from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


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


class Project(models.Model):    
    posted = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to = 'projects/')
    title = models.CharField(max_length =30)    
    link = models.CharField(max_length =150)
    description = HTMLField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    design_score = models.IntegerField(default=0)
    usability_score = models.IntegerField(default=0)
    content_score = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_description(self):
        self.save()


class Rating(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    design_score = models.IntegerField(default=0)
    usability_score = models.IntegerField(default=0)
    content_score = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)
    rated_by = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.overall_score


class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote