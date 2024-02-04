from django.shortcuts import render, redirect, HttpResponse
from . import forms 
from . import models

def file_upload(request):
    form = forms.UploadFileForm(request.POST, request.FILES)
    
    if request.method == "POST":
        files = request.FILES.getlist("file")
        for file in files:
            file_ins = models.File(file = file)
            file_ins.save()
        return redirect("success")
    
    return render(request, "upload.html", {"form": form})

def upload_success(request):
    return render(request, "success.html")