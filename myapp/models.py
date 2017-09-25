from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Address_Detail(models.Model):
    current_address = models.CharField(max_length=40, default=None, primary_key=True)
    current_city = models.CharField(max_length=40, default=None)
    current_province = models.CharField(max_length=40, default=None)
    current_country = models.CharField(max_length=40, default=None)
    mailing_address = models.CharField(max_length=60, default=None)
    mailing_city = models.CharField(max_length=40, default=None)
    mailing_state = models.CharField(max_length=40, default=None)
    mailing_country = models.CharField(max_length=40, default=None)

    def __str__(self):
        return str(self.current_address)


class Certification_Detail(models.Model):
    certi_title = models.CharField(max_length=40, default=None)
    certi_body = models.CharField(max_length=40, default=None)

    def __str__(self):
        return str(self.certi_title)


class Company_Detail(models.Model):
    company_address = models.CharField(max_length=80, default=None)
    company_city = models.CharField(max_length=40, default='Windsor')
    company_province = models.CharField(max_length=40, default='Ontario')
    company_postalcode = models.CharField(max_length=40, default=None)
    company_country = models.CharField(max_length=40, default='Canada')
    company_contact_fname = models.CharField(max_length=40, default=None)
    company_contact_lname = models.CharField(max_length=40, default=None)
    company_contact_position = models.CharField(max_length=40, default=None)
    company_phone = models.IntegerField(default=None)
    company_email = models.EmailField(default=None)
    company_website = models.URLField(default=None)
    company_note = models.TextField(default=None)
    certification_detail = models.ForeignKey(Certification_Detail, default=None)

    def __str__(self):
        return str(self.company_website)


class Internship_Type(models.Model):
    internship_type = models.CharField(max_length=80, default=None)

    def _str_(self):
        return str(self.internship_type)


class Job_Group(models.Model):
    job_group_description = models.CharField(max_length=40, default=None)

    def __str__(self):
        return str(self.job_group_description)


class Job_Requirment(models.Model):
    job_req_desc = models.CharField(max_length=60, default=None)

    def _str_(self):
        return str(self.job_req_desc)


class Job_Responsibilities(models.Model):
    job_resp_desc = models.CharField(max_length=60, default=None)

    def _str_(self):
        return str(self.job_resp_desc)


class Job_Status(models.Model):
    STATUS_CHOICES = (
        ('un', 'Unopened'),
        ('op', 'Open'),
        ('cl', 'Closed')
    )
    job_status = models.CharField(max_length=60, choices=STATUS_CHOICES,default=None)

    def __str__(self):
        return str(self.job_status)


class Job_Detail(models.Model):
    job_group = models.ForeignKey(Job_Group, default=None)
    job_company = models.ForeignKey(Company_Detail, default=None)
    job_internship_type = models.ForeignKey(Internship_Type, default=None)
    job_position = models.CharField(max_length=60, default=None)
    job_description = models.CharField(max_length=40, default=None)
    job_requirment = models.ForeignKey(Job_Requirment, default=None)
    job_responsibility = models.ForeignKey(Job_Responsibilities, default=None)
    job_salery = models.CharField(max_length=40, default=None)
    job_status = models.ForeignKey(Job_Status, default=None)

    def __str__(self):
        return str(self.job_company)


class Student_Detail(models.Model):
    student_fname = models.CharField(max_length=40, default=None)
    student_mname = models.CharField(max_length=40, default=None)
    student_lname = models.CharField(max_length=40, default=None)
    student_phone = models.IntegerField(default=None)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    student_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    STATUS_CHOICES = (
        ('i', 'International'),
        ('p', 'Permanent Resident')
    )
    student_choice = models.CharField(max_length=1, choices=STATUS_CHOICES, default=None)
    CURRENT_PAST_CHOICES = (
        ('cs', 'Current Student'),
        ('ps', 'Past Student')
    )
    student_current_past_choices = models.CharField(max_length=2, choices=CURRENT_PAST_CHOICES, default=None)

    def __str__(self):
        return str(self.student_fname)


class Education_Detail(models.Model):
    degree_name = models.CharField(max_length=40, default=None)
    degree_title = models.CharField(max_length=40, default=None)
    degree_cpga = models.CharField(max_length=40, default=None)
    degree_university = models.CharField(max_length=60, default=None)
    degree_university_location = models.CharField(max_length=60, default=None)
    degree_start_month = models.IntegerField(default=None)
    degree_end_month = models.IntegerField(default=None)
    degree_start_year = models.IntegerField(default=None)
    degree_end_year = models.IntegerField(default=None)
    st_fname = models.ForeignKey(Student_Detail, default=None)

    def __str__(self):
        return str(self.degree_name)



class Semester_Registered(models.Model):
    semester = models.CharField(max_length=60, default=None)
    semester_year = models.IntegerField(default=None)
    student_detail = models.ForeignKey(Student_Detail, default=None)

    def __str__(self):
        return str(self.semester)


class Student_Internship_Detail(models.Model):
    job_detail = models.ForeignKey(Job_Detail, default=None)


class User_Auth(User):
    usr_id = models.CharField(max_length=40, default=None)


class Group(models.Model):
    GROUP_CHOICES = (
        ('st', 'Student'),
        ('fc', 'Faculty'),
        ('sf', 'Staff')
    )
    group_name = models.CharField(max_length=20, choices=GROUP_CHOICES, null=True)
    user_group = models.ForeignKey(User_Auth, default=None)

    def __str__(self):
        return self.group_name
