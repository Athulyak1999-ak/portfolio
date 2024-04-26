from django.contrib import admin
from .models import UserProfile, Project, Education, Certification
from .models import UserProfile, Project, Education, WorkExperience, Certification, Image_Add


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(WorkExperience)
admin.site.register(Image_Add)