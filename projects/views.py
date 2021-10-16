from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
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


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'projects/project_form.html', context)