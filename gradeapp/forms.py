from django import forms
from .models import Profile, Project

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['posted', 'profile', 'design_score', 'usability_score', 'content_score', 'overall_score']
        widgets = {
            'link': forms.TextInput(attrs={'placeholder': 'https://myapp.com/'}),            
        }