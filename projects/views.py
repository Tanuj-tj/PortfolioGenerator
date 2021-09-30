from django.shortcuts import render
from django.http.response import HttpResponse

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
    page = 'Hello How are you'
    number = 8
    context = {
        'page' : page,
        'number':number,
        'projects': projectsList,
    }
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})

