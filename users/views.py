from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        username = request.POST('username')
        password = request.POST('password')

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")
        
        user = authenticate(request, username=username,password=password)

    return render(request,'users/login_register.html')    

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile':profile,
        'topSkills' : topSkills,
        'otherSkills':otherSkills,
    }
    return render(request,'users/user-profile.html',context)