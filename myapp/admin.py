from django.contrib import admin
from .models import Company_Detail, Certification_Detail, Address_Detail, Education_Detail, Internship_Type, Job_Group,\
    Job_Detail, Job_Status, Job_Responsibilities, Job_Requirment, Semester_Registered, \
    Student_Internship_Detail, User_Auth, Group

# Register your models here.

admin.site.register(Company_Detail),
admin.site.register(Certification_Detail),
admin.site.register(Address_Detail),
admin.site.register(Education_Detail),
admin.site.register(Internship_Type),
admin.site.register(Job_Group),
admin.site.register(Job_Detail),
admin.site.register(Job_Status),
admin.site.register(Job_Requirment),
admin.site.register(Job_Responsibilities),
admin.site.register(Semester_Registered),
admin.site.register(Student_Internship_Detail),
admin.site.register(User_Auth),
admin.site.register(Group),
