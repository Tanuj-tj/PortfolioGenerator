from django.forms import ModelForm
from django import forms
from .models import Project, Review

# This will generate a form based on what we have in the model
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title',
                  'featured_image',
                  'description',
                  'demo_link',
                  'source_link',
                   'tags']


        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({ 'class':'input'})

        # self.fields['title'].widget.attrs.update({ 'class':'input'})

        # self.fields['description'].widget.attrs.update({ 'class':'input'})



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
    
        labels = {
            'value':'Place your vote',
            'body':'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({ 'class':'input'})