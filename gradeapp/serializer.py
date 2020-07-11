from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class ProfileSerializer(serializers.ModelSerializer):
    account_holder = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()    
    class Meta:
        model = Project
        fields = '__all__'