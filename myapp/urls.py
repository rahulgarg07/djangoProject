from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^companydetail[/]$', views.company_detail, name='Company Details'),
        url(r'^addcompanydetail[/]$', views.add_company_details, name='Add Company Details'),
        url(r'^certificationdetail[/]$', views.certification_deatil, name='Certification Details'),
        url(r'^addcertificationdetail[/]$', views.add_certification_detail, name='Add Certification Details'),
        url(r'^jobdetail[/]$', views.job_details, name='Job Details'),
        url(r'^addjobdetail[/]$', views.add_job_details, name='Add Job Details'),
        url(r'^internshiptype[/]$', views.internship_type, name='Internship Type'),
        url(r'^addinternshiptype[/]$', views.add_internship_type, name='Add Internship Type'),
        url(r'^jobgroup[/]$', views.job_group, name='Job Group'),
        url(r'^addjobgroup[/]$', views.add_job_group, name='Add Job Group'),
        url(r'^jobresponsibility[/]$', views.job_responsibility, name='Job Responsibility'),
        url(r'^addjobresponsibility[/]$', views.add_job_responsibility, name='Add Job Responsibility'),
        url(r'^jobrequirment[/]$', views.job_requirment, name='Job Requirment'),
        url(r'^addjobrequirment[/]$', views.add_job_requirment, name='Add Job Requirment'),
        url(r'^jobstatus[/]$', views.job_status, name='Job Status'),
        url(r'^addjobstatus[/]$', views.add_job_status, name='Add Job Status'),
        url(r'^studentdetail[/]$', views.student_detail, name='Student Details'),
        url(r'^addstudentdetail[/]$', views.add_student_detail, name='Add Student Details'),
        url(r'login[/]?$', views.user_login, name='login'),
        url(r'^logout[/]$', views.logout, name='Logout'),
        url(r'^register[/]$', views.register, name='Register'),
        url(r'^group[/]$', views.group, name='Group'),
        url(r'^addgroup[/]$', views.addgroup, name='Add Group'),
        url(r'^educationdetail[/]$', views.education_detail, name='Education Details'),
        url(r'^addeducationdetail[/]$', views.add_education_detail, name='Add Education Details'),

]