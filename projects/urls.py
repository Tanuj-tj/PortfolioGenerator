from django.contrib import admin
from django.urls import path
from django.http.response import HttpResponse
from . import views

urlpatterns = [
    path('', views.projects,name = "projects"),
    path('project/<str:pk>/', views.project,name = "project"),
]
