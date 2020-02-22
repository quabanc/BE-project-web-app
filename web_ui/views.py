from django.shortcuts import render

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
    return render(request, "created_quiz.html", {})