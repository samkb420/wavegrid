from django.forms import ModelForm 
from django import forms
from .models import *

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

class AddProjectImagesForm(ModelForm):

    class Meta:
        model = ProjectImages
        fields = '__all__'
        widgets = {
            'image':forms.FileInput(attrs={'multiple':True})
        }  

class ProjectsForm(ModelForm):
    more_project_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
                    'class':'form-control',
                    'multiple':True
                    }))
    class Meta:
        model = Projects
        fields = '__all__'

        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'   

class PartnersForm(ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'          