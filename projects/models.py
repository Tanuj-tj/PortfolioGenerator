from typing import ChainMap
from django.core.exceptions import MiddlewareNotUsed
from django.db import models
from users.models import Profile
import uuid

# Create your models here.

class Project(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    
    featured_image = models.ImageField(blank=True,null=True,default="default.jpg")
    
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    # Override the id attribure
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total','title']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

    
# MANY TO ONE RELATION

class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    ''' Creating a project attribure in Review table which is referening to the id (PK) attribure of Project table 
        models.CASCADE means that the reviews will get deleted if the project is deleted 
    '''


    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value



# MANY TO MANY RELATION

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name