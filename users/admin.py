from django.contrib import admin

# Register your models here.

from .models import Profile, Skills

admin.site.register(Profile)
admin.site.register(Skills)
