from django.shortcuts import render
from .models import UserProfile, Project, Education, WorkExperience, Certification, Image_Add

# Create your views here.
def portfolio_showcase(request):
    users = UserProfile.objects.all()
    project = Project.objects.all()
    certification = Certification.objects.all()
    experience = WorkExperience.objects.all()
    pic = Image_Add.objects.all()
    education = Education.objects.all()
    return render(request, 'index.html', {'users': users, 'project': project, 'certification': certification, 'experience': experience, 'pic': pic, 'education': education})








