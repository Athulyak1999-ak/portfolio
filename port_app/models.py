from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=200,blank=True)
    biography = models.TextField(blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True)
    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Image_Add(models.Model):
    image = models.ImageField(upload_to="pictures")


class Education(models.Model):
    institute = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.degree} from {self.institute}"

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    def __str__(self):
        return f"{self.position} at {self.company}"



class Certification(models.Model):
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    date_received = models.DateField()

    def __str__(self):
        return self.name


