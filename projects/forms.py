from django.forms import ModelForm
from .models import Project

# This will generate a form based on what we have in the model
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'