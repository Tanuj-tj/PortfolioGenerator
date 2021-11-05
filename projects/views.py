from django.core import paginator
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Review,Tag
from .forms import ProjectForm, ReviewForm
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
    form = ReviewForm()
    tags = projectObj.tags.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        # Update project votecount
        messages.success(request, 'Your review was successfully submitted')
        return redirect('project', pk=projectObj.id)

    context = {
        'project':projectObj,  
        'tags' : tags,
        'form':form,  
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