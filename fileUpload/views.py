import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponse, Http404
import pandas as pd



class Home(TemplateView):
    template_name = 'home.html'

def login(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        password = request.POST["psw"]
        if username == 'admin' and password == 'admin':
            return redirect('showlist')
        else:
            messages.error(request,'Enter correct Username or Password')
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def upload(request):    
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)               
    return render(request, 'upload.html')

def showlist(request):
    total_files = os.listdir(settings.MEDIA_ROOT)
    print(total_files)
    return render(request,'list.html',{'total_files':total_files})

  
def open(request,file_name):
    if file_name  in os.listdir(settings.MEDIA_ROOT):
       if ".csv" in file_name:
            file = pd.read_csv(os.path.join(settings.MEDIA_ROOT,file_name))
       else:
            file = pd.read_excel(os.path.join(settings.MEDIA_ROOT,file_name)) 
    
       data_object = file.to_html()
       return HttpResponse(data_object)
    else:
        return  HttpResponse(Http404) 
    
    



