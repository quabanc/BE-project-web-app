from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from web_ui.models import MultiUser, Image, Option, Question, Quiz
import requests


@login_required
def index_view(request):
    user = MultiUser.objects.get(email=request.user.username)
    if user.user_type == 'STUDENT':
        template = 'index.html'
    elif user.user_type == 'TEACHER':
        template = 'teacher.html'

    return render(request, template, {})


def register_view(request):
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user = MultiUser.objects.create(
            username=email,
            email=email,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        user = User.objects.get(username=email)
        login(request, user)
        return redirect("index")
    return render(request, 'register.html', {})


def login_view(request):
    if request.POST:
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, 'login.html', {})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, 'profile.html', {})



@login_required
def quiz_view(request):
    return render(request, 'quiz.html', {})


@login_required
def completed_quiz_view(request):
    return render(request, "completed_quiz.html", {})


@login_required
def created_quiz_view(request):
    user = MultiUser.objects.get(email=request.user.username)

    if user.user_type == "TEACHER":
        if request.POST:
            quiz_name = request.POST["quiz_name"]
            quiz_model = Quiz.objects.create(quiz_name=quiz_name)

            images = dict(request.FILES)['images']
            captions = []
            options_all = []
            url = 'http://127.0.0.1:5000/upload'


            for image in images:
                image_model = Image(image=image)
                image_model.save()
                file = {'image': open(image_model.image.url[7:], 'rb')}
                res = requests.post(url, files=file)
                
                caption = res.json()['caption']
                options = res.json()['options']

                # Database stuff
                question_model = Question.objects.create(
                    image=image_model.image.url[7:],
                    caption=caption
                )
                for option in options:
                    option_model = Option.objects.create(
                        option=option[0],
                        correct=option[1]["correct"]
                    )
                    question_model.options.add(option_model)
                    option_model.save()
                question_model.save()
                quiz_model.questions.add(question_model)

                captions.append(caption)
                options_all.append(options)
                print(options)
            quiz_model.save()
            
            return render(request, "created_quiz.html", {'images': zip(images, captions, options_all), 'len': len(images)})
    return redirect("index")
