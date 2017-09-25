from django import forms
from myapp.models import Company_Detail,Certification_Detail, Job_Detail, Internship_Type, Job_Group, \
    Job_Responsibilities, Job_Requirment, Job_Status, Student_Detail, User_Auth, Group, Education_Detail



class Company_DetailForm(forms.ModelForm):
    class Meta:
        model = Company_Detail
        fields = ['company_address', 'company_city', 'company_province', 'company_postalcode', 'company_country',
                  'company_contact_fname', 'company_contact_lname', 'company_contact_position', 'company_phone',
                  'company_email', 'company_website', 'company_note', 'certification_detail']
        widgets = {'company_note': forms.Textarea}
        labels = {'company_address': u'Company Address', 'company_city': u'City', 'company_province': u'Province',
                  'company_postalcode': u'Postal Code', 'company_country': u'Country',
                  'company_contact_fname': u'Contact First Name', 'company_contact_lname': u'Contact Last Name',
                  'company_contact_position': u'Contact Position', 'company_phone': u'Company Phone Number',
                  'company_email': u"Company's Email Address", 'company_website': u"Company's Web Address",
                  'company_note': u'Notes', 'certification_detail': u'Certification Details'}


class Certification_DetailForm(forms.ModelForm):
    class Meta:
        model = Certification_Detail
        fields = ['certi_title', 'certi_body']
        labels = {'certi_title': u'Certification Title', 'certi_body': u'Certification Body'}


class Job_DetailForm(forms.ModelForm):
    class Meta:
        model = Job_Detail
        fields = ['job_group', 'job_company', 'job_internship_type', 'job_position', 'job_description', 'job_requirment'
                  , 'job_responsibility', 'job_status', 'job_salery']


class Internship_TypeForm(forms.ModelForm):
    class Meta:
        model = Internship_Type
        fields = {'internship_type'}
        labels = {'internship_type': u'Internship Type'}


class Job_GroupForm(forms.ModelForm):
    class Meta:
        model = Job_Group
        fields = {'job_group_description'}
        labels = {'job_group_description': u'Job Group Name'}


class Job_ResponsibilityForm(forms.ModelForm):
    class Meta:
        model = Job_Responsibilities
        fields = {'job_resp_desc'}
        labels = {'job_resp_desc': u'Job Respinsibility Description'}


class Job_RequirmentForm(forms.ModelForm):
    class Meta:
        model = Job_Requirment
        fields = {'job_req_desc'}
        labels = {'job_req_desc': u'Job Requirment Description'}


class Job_StatusForm(forms.ModelForm):
    class Meta:
        model = Job_Status
        fields = {'job_status'}
        labels = {'job_status': u'Job Status'}


class Student_DetailForm(forms.ModelForm):
    class Meta:
        model = Student_Detail
        fields = ['student_fname', 'student_mname', 'student_lname', 'student_phone', 'student_gender', 'student_choice',
                  'student_current_past_choices']
        labels = {'student_fname': u'First Name', 'student_mname': u'Middle Name', 'student_lname': u'Last Name',
                  'student_phone': u'Phone Number', 'student_gender': u'Gender', 'student_choice': u'Student Choice',
                  'student_current_past_choices': u'Current and past choices'}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User_Auth
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'usr_id']
        widgets = {'password': forms.PasswordInput(), }
        labels = {'first_name': u'First Name', 'last_name': u'Last Name', 'username': u'User Name', 'password':
                  u'Password', 'email': u'Email', 'usr_id': u'User Id'}



class LoginForm(forms.ModelForm):
    class Meta:
        model = User_Auth
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}
        labels = {'username': u'User Name', 'password': u'Password'}


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'user_group']
        labels = {'group_name': u'Group Name', 'user_group': u'User Group'}



class Education_DetailForm(forms.ModelForm):
    class Meta:
        model = Education_Detail
        fields = ['degree_name', 'degree_title', 'degree_cpga', 'degree_university', 'degree_university_location',
                  'degree_start_month', 'degree_end_month', 'degree_start_year', 'degree_end_year', 'st_fname']
        labels = {'degree_name': u'Degree Name', 'degree_title': u'Degree Title', 'degree_cpga': u'Cpga',
                  'degree_university': u'University Name', 'degree_university_location': u'University Location',
                  'degree_start_month': u'Starting Month', 'degree_end_month': u'Ending Month',
                  'degree_start_year': u'Starting Year', 'degree_end_year': u'Ending Year', 'st_fname': u'Student Name'}

