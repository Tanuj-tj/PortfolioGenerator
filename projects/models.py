from typing import ChainMap
from django.core.exceptions import MiddlewareNotUsed
from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    # Override the id attribure
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title


# MANY TO ONE RELATION

class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    ''' Creating a project attribure in Review table which is referening to the id (PK) attribure of Project table 
        models.CASCADE means that the reviews will get deleted if the project is deleted 
    '''


    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)


    def __str__(self):
        return self.value



# MANY TO MANY RELATION

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name