from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Project

projectsList = [
    {
        'id' : '1',
        'title' : "Ecommerce Website",
        'description' : 'Fully functional ecommerce website'
    },

    {
        'id' : '2',
        'title' : "Portfilio Website",
        'description' : 'This was a project where I buit out my portfolio'
    },

    {
        'id' : '3',
        'title' : "Social Network",
        'description' : 'Awsome open source project I am still working on'
    }
]

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