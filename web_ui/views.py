from django.shortcuts import render
from .models import Image
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

    for i in images:
        model.image = i
        model.save()
    
    
    return render(request, "created_quiz.html", {'images': images, 'len': len(images)})

def upload_files(request):
    
    
    return render(request, "index.html", {})