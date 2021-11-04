from django.core import paginator
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project,Tag
from .forms import ProjectForm
from .utils import searchProjects, paginateProject

def projects(request):

    projects, search_query = searchProjects(request)

    custom_range,projects = paginateProject(request,projects,6)

    context = {
        'projects': projects,
        'seach_query':search_query,
        #'paginator' : paginator,
        'custom_range':custom_range,
    }
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {
        'project':projectObj,  
        'tags' : tags,  
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {
        'form' : form
    }
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form' : form
    }

    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}

    return render(request, 'delete_template.html',context)