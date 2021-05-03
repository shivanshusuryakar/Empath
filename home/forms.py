from django.forms import ModelForm
from .models import Imagemodel

class ImageForm(ModelForm):
    class Meta:
        model=Imagemodel
        fields=['faceimg']