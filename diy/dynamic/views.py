from django.shortcuts import render, get_object_or_404
from .models import DIYProject

def project_list(request):
    projects = DIYProject.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(DIYProject, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def bot(request):
    return render(request,'bot.html')

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')
