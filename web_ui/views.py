from django.shortcuts import render
from .models import Image
import requests
# Create your views here.



def index_view(request):
    user = 'teacher' # Just for testing purpose
    if user == 'student':
        template = 'index.html'
    else:
        template = 'teacher.html'

    return render(request, template, {})

def register_view(request):
    return render(request, 'register.html', {})

def login_view(request):
    return render(request, 'login.html', {})

def profile_view(request):
    return render(request, 'profile.html', {})

def quiz_view(request):
    return render(request, 'quiz.html', {})

def completed_quiz_view(request):
    return render(request, "completed_quiz.html", {})

def created_quiz_view(request):
    images = dict(request.FILES)['images']
    model = Image()
    captions = []
    url = 'http://127.0.0.1:5000/upload'


    for i in images:
        model.image = i
        model.save()
        file = {'image': open(model.image.url[7:], 'rb')}
        res = requests.post(url, files=file)
        caption = res.json()['caption']
        captions.append(caption)
    
    return render(request, "created_quiz.html", {'images': zip(images, captions), 'len': len(images)})
