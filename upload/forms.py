from django import forms
from . import models

class UploadFileForm(forms.ModelForm):
    file = forms.FileField(
        widget = forms.TextInput(attrs={
            "name": "files",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }),
        label = ""
    )
    
    class Meta:
        model = models.File
        fields = ["file"]