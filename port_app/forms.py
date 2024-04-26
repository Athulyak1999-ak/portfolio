from django import forms
from .models import UserProfile, Project, Education, Certification

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class EductionForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"

