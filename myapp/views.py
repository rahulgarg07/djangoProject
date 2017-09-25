from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session
from myapp.models import Company_Detail, Job_Detail, Internship_Type, Job_Group, Job_Responsibilities, Job_Requirment, \
    Job_Status, Certification_Detail, Student_Detail, User_Auth, Group, Education_Detail
from django.shortcuts import get_object_or_404
from myapp.forms import Company_DetailForm, Job_DetailForm, Internship_TypeForm, Job_GroupForm, Job_ResponsibilityForm, \
    Job_RequirmentForm, Job_StatusForm, Certification_DetailForm, Student_DetailForm, RegisterForm, LoginForm, \
    GroupForm, Education_DetailForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.



def index(request):
    studentlist = User_Auth.objects.all()
    return render(request, 'myapp/index.html', {'studentlist': studentlist})


def company_detail(request):
    com_detail = Company_Detail.objects.all()
    return render(request, 'myapp/companydetail.html', {'com_detail': com_detail})


def certification_deatil(request):
    cert_detail = Certification_Detail.objects.all()
    sfuser = User_Auth.objects.get(group__group_name='sf')
    fcuser = User_Auth.objects.get(group__group_name='fc')
    #stuser = User_Auth.objects.get(group__group_name='st')  # Not needed for this loop. #Part of 'Student loop'.
    if sfuser != 0 or fcuser !=0:
        if str(sfuser.username) == request.session.get('username') or str(fcuser.username) == request.session.get(
                'username'):
            return render(request, 'myapp/certificationdetail.html', {'cert_detail': cert_detail})
        # Code not needed.// 'Student loop'
        # else:
        #     if stuser !=0:
        #         if str(stuser.username) == request.session.get('username'):
        #             return render(request, 'myapp/jobdetail.html')
        #     else:
        #         return HttpResponse('Invalid Login credentials.')
    else:        #To add Student loop, remove this.
        HttpResponse('Invalid login details.')



def add_certification_detail(request):
    cert_detail = Certification_Detail.objects.all()
    user = User_Auth.objects.get(group__group_name='sf')
    if user !=0:
        if str(user.username) == request.session.get('username'):
            if request.method == 'POST':
                form = Certification_DetailForm(request.POST)
                if form.is_valid():
                    cer_detail = form.save(commit=False)
                    cer_detail.num_responses = 1
                    cer_detail.save()
                    return HttpResponseRedirect('/myapp/certificationdetail/')
            else:
                form = Certification_DetailForm()
                return render(request, 'myapp/addcertificationdetail.html', {'cert_detail': cert_detail,
                                                                             'form': form})
        else:
            HttpResponseRedirect('/myapp/login/')
    else:
        HttpResponseRedirect('/myapp/login/')


def add_company_details(request):
    com_detail = Company_Detail.objects.all()
    if request.method == 'POST':
        form = Company_DetailForm(request.POST)
        if form.is_valid():
            comp_detail = form.save(commit=False)
            comp_detail.num_responses = 1
            comp_detail.save()
            return HttpResponseRedirect('/myapp/companydetail/')
    else:
        form = Company_DetailForm()
        return render(request, 'myapp/addcompanydetail.html', {'form': form,
                                                               'com_detail': com_detail})


def job_details(request):
    j_detail = Job_Detail.objects.all()
    return render(request, 'myapp/jobdetail.html', {'j_detail': j_detail})


def add_job_details(request):
    j_detail = Job_Detail.objects.all()
    if request.method == 'POST':
        form = Job_DetailForm(request.POST)
        if form.is_valid():
            jo_detail = form.save(commit=False)
            jo_detail.num_responses = 1
            jo_detail.save()
        return HttpResponseRedirect('/myapp/jobdetail/')
    else:
        form = Job_DetailForm()
        return render(request, 'myapp/addcompanydetail.html', {'j_detail': j_detail,
                                                               'form': form})


def internship_type(request):
    int_detail = Internship_Type.objects.all()
    return render(request, 'myapp/internshiptype.html', {'int_detail': int_detail})


def add_internship_type(request):
    int_detail = Internship_Type.objects.all()
    if request.method == 'POST':
        form = Internship_TypeForm(request.POST)
        if form.is_valid():
            in_detail = form.save(commit=False)
            in_detail.num_responses = 1
            in_detail.save()
            return HttpResponseRedirect('/myapp/internshiptype/')
    else:
        form = Internship_TypeForm()
        return render(request, 'myapp/addinternshiptype.html', {'int_detail': int_detail,
                                                                'form': form})


def job_group(request):
    job_detail = Job_Group.objects.all()
    return render(request, 'myapp/jobgroup.html', {'job_detail': job_detail})


def add_job_group(request):
    job_detail = Job_Group.objects.all()
    if request.method == 'POST':
        form = Job_GroupForm(request.POST)
        if form.is_valid():
            joo_detail = form.save(commit=False)
            joo_detail.num_responses = 1
            joo_detail.save()
            return HttpResponseRedirect('/myapp/jobgroup/')
    else:
        form = Job_GroupForm
        return render(request, 'myapp/addjobgroup.html', {'job_detail': job_detail,
                                                          'form': form})


def job_responsibility(request):
    job_res = Job_Responsibilities.objects.all()
    return render(request, 'myapp/jobresponsibilities.html', {'job_res': job_res})


def add_job_responsibility(request):
    job_res = Job_Responsibilities.objects.all()
    if request.method == 'POST':
        form = Job_ResponsibilityForm(request.POST)
        if form.is_valid():
            jo_res = form.save(commit=False)
            jo_res.num_responses = 1
            jo_res.save()
            return HttpResponseRedirect('/myapp/jobresponsibility/')
    else:
        form = Job_ResponsibilityForm()
        return render(request, 'myapp/addjobresponsibilities.html', {'form': form,
                                                                     'job_res': job_res})


def job_requirment(request):
    job_detail = Job_Requirment.objects.all()
    return render(request, 'myapp/jobrequirment.html', {'job_detail': job_detail})


def add_job_requirment(request):
    job_req = Job_Requirment.objects.all()
    if request.method == 'POST':
        form = Job_RequirmentForm(request.POST)
        if form.is_valid():
            jo_req = form.save(commit=False)
            jo_req.num_responses = 1
            jo_req.save()
            return HttpResponseRedirect('/myapp/jobrequirment/')
    else:
        form = Job_RequirmentForm()
        return render(request, 'myapp/addjobrequirment.html', {'form': form,
                                                               'job_req': job_req})


def job_status(request):
    job_st = Job_Status.objects.all()
    return render(request, 'myapp/jobstatus.html', {'job_st': job_st})


def add_job_status(request):
    job_st = Job_Status.objects.all()
    if request.method == 'POST':
        form = Job_StatusForm(request.POST)
        if form.is_valid():
            jo_st = form.save(commit=False)
            jo_st.num_responses = 1
            jo_st.save()
            return HttpResponseRedirect('/myapp/jobstatus/')
    else:
        form = Job_StatusForm()
        return render(request, 'myapp/addjobstatus.html', {'form': form,
                                                           'job_st': job_st})


def student_detail(request):
    st_det = Student_Detail.objects.all()
    return  render(request, 'myapp/studentdetail.html', {'st_det': st_det})



def add_student_detail(request):
    st_det = Student_Detail.objects.all()
    if request.method == 'POST':
        form = Student_DetailForm(request.POST)
        if form.is_valid():
            st_de = form.save(commit=False)
            st_de.num_responses = 1
            st_de.save()
            return HttpResponseRedirect('/myapp/studentdetail/')
    else:
        form = Student_DetailForm()
        return render(request, 'myapp/addstudentdetail.html', {'form': form,
                                                                   'st_det': st_det})


def education_detail(request):
    edu = Education_Detail.objects.all()
    sfuser = User_Auth.objects.get(group__group_name='sf')
    fcuser = User_Auth.objects.get(group__group_name='fc')
    if sfuser != 0 or fcuser != 0:
        if str(sfuser.username) == request.session.get('username') or str(fcuser.username) == request.session.get(
                'username'):
            return render(request, 'myapp/educationdetail.html', {'edu': edu})
    else:
        HttpResponse('Invalid login details.')


def add_education_detail(request):
    edu = Education_Detail.objects.all()
    if request.method == 'POST':
        form = Education_DetailForm(request.POST)
        if form.is_valid():
            ed = form.save(commit=False)
            ed.num_responses = 1
            ed.save()
        return HttpResponseRedirect('/myapp/educationdetail/')
    else:
        form = Education_DetailForm()
        return render(request, 'myapp/addeducationdetail.html', {'form': form,
                                                                 'edu': edu})


def register(request):
    userlist = User_Auth.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.set_password(form.cleaned_data['password'])
            student.save()
            return HttpResponseRedirect('/myapp/')
    else:
        form = RegisterForm()
    return render(request, "myapp/register.html", {'form': form, 'userlist': userlist})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                return render(request, 'myapp/index.html', {'username': username, 'user': user})  #
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        form = LoginForm()
        return render(request, 'myapp/login.html', {'form': form})




@login_required(login_url="/myapp/login", redirect_field_name='')


def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return  HttpResponseRedirect(reverse('myapp:index'))


def group(request):
    grp = Group.objects.all()
    return render(request, 'myapp/group.html', {'grp': grp})


def addgroup(request):
    grp = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            gr = form.save(commit=False)
            gr.num_responses = 1
            gr.save()
            return HttpResponseRedirect('/myapp/group/')
    else:
        form = GroupForm()
        return render(request, 'myapp/addgroup.html', {'form': form,
                                                       'grp': grp})



