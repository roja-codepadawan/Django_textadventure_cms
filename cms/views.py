from django.shortcuts import render
from .models import Story

def home(request):
    stories = Story.objects.all()
    return render(request, 'home.html', {'stories': stories})
