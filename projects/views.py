from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
import requests
import os

# Create your views here.
def home(request):
    pas = os.environ.get('EMAIL_PASSWORD')
    print(pas)
    return render(request,'projects/home.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    context = {
        'form' : form,
    }
    return render(request,'projects/register.html',context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, 'projects/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

def profile(request):
    form = ClientProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ClientProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            cid = User.objects.filter(username=request.user)
            Client.objects.filter(user=cid[0]).delete()
            usr = request.user
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            profession = form.cleaned_data['profession']
            age = form.cleaned_data['age']
            organization = form.cleaned_data['organization']
            address = form.cleaned_data['address']
            ctag = form.cleaned_data['ctag']
            portfolio = form.cleaned_data['portfolio']
            email = request.user.email
            github = form.cleaned_data['github']
            myapi = f"https://api.github.com/users/{github}"
            json_data = requests.get(myapi).json()
            print(json_data)
            client_profile = Client(user=usr,name=name,phone=phone,age=age,address=address,profession=profession,organization=organization,ctag=ctag,portfolio=portfolio,email=email)
            client_profile.save()
            return redirect('home')
    context = {
        'form' : form,
    }
    return render(request,'projects/profile.html',context)

def addProjects(request):
    form = ClientAddProject(instance=request.user)
    if request.method == 'POST':
        form = ClientAddProject(request.POST, instance=request.user)
        if form.is_valid():
            usr = request.user
            title = form.cleaned_data['title']
            tag = form.cleaned_data['tag']
            description = form.cleaned_data['description']
            created = form.cleaned_data['created']
            completed = form.cleaned_data['completed']
            achievements = form.cleaned_data['achievements']
            tech = form.cleaned_data['tech']
            github = form.cleaned_data['github']
            live = form.cleaned_data['live']
            opf1 = form.cleaned_data['opf1']
            opfl1 = form.cleaned_data['opfl1']
            opf2 = form.cleaned_data['opf2']
            opfl2 = form.cleaned_data['opfl2']
            opf3 = form.cleaned_data['opf3']
            opfl3 = form.cleaned_data['opfl3']
            opf4 = form.cleaned_data['opf4']
            opfl4 = form.cleaned_data['opfl4']
            imgl = form.cleaned_data['imgl']
            
            add_project = Project(user=usr,title=title,tag=tag,description=description,created=created,completed=completed,achievements=achievements,tech=tech,github=github,live=live,opf1=opf1,opfl1=opfl1,opf2=opf2,opfl2=opfl2,opf3=opf3,opfl3=opfl3,opf4=opf4,opfl4=opfl4,imgl=imgl)
            add_project.save()
            return redirect(f'/user/{usr}')
    context = {
        'form' : form,
    }
    return render(request,'projects/addProjects.html',context)

def myProjects(request):
    usr = request.user
    projects = Project.objects.filter(user=usr)
    context = {
        'projects' : projects
    }
    return render(request,'projects/myProjects.html',context)

def confirmDelete(request,pid):
    project = Project.objects.filter(id=pid)
    context = {
        'project' : project
    }
    return render(request,'projects/confirmDelete.html',context)

def delProjects(request,pid):
    Project.objects.filter(id=pid).delete()
    return render(request,'projects/deleted.html')

def viewProjects(request,pk):
    cid = User.objects.filter(username=pk)
    projects = Project.objects.filter(user=cid[0])
    profile = Client.objects.filter(user=cid[0])
    print(profile)
    context = {
        'profile' : profile,
        'projects' : projects
    }
    return render(request,'projects/viewProjects.html',context)

def onlyProject(request,pid):
    project = Project.objects.filter(id=pid)
    context = {
        'project' : project
    }
    return render(request,'projects/onlyProject.html',context)




