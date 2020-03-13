from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from web_ui.models import MultiUser, Image, Option, Question, Quiz, QuizCompleted, QuestionsCompleted
import requests


@login_required
def index_view(request):
    user = MultiUser.objects.get(email=request.user.username)
    if user.user_type == 'STUDENT':
        template = 'index.html'

        # Quizes completed by the user
        quiz_completed = [quiz.quiz for quiz in user.quiz_completed.all()]
        quiz_pending = []
        all_quizes = list(Quiz.objects.all())
        for quiz in all_quizes:
            if quiz not in quiz_completed:
                quiz_pending.append(quiz)

        return render(request, template, {"quiz_completed": quiz_completed, "quiz_pending": quiz_pending})
    elif user.user_type == 'TEACHER':
        template = 'teacher.html'
        quizes = Quiz.objects.all()
        return render(request, template, {"quizes": quizes})
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
            
            return redirect("uploaded_quiz", quiz_name=quiz_model.quiz_name)
            # return render(request, "created_quiz.html", {'images': zip(images, captions, options_all), 'len': len(images)})
    return redirect("index")


@login_required
def uploaded_quiz(request, quiz_name):
    quiz = Quiz.objects.get(quiz_name=quiz_name)
    questions = {}
    for question in quiz.questions.all():
        questions[question.id] = {
            "caption": question.caption,
            "image": question.image[14:],
            "options": question.options.all()
        }
    return render(request, "uploaded_quiz.html", {"quiz_name": quiz_name, "questions": questions})


@login_required
def pending_quiz(request, quiz_name):
    quiz = Quiz.objects.get(quiz_name=quiz_name)

    if request.POST:
        question_answers = dict(request.POST)
        del question_answers["csrfmiddlewaretoken"]

        quiz_completed = QuizCompleted.objects.create(quiz=quiz)
        for caption in question_answers:
            question = quiz.questions.get(caption=caption)
            option_selected = question_answers[caption][0]
            correct = question.options.get(option=option_selected).correct
            
            question_completed = QuestionsCompleted.objects.create(
                question=question,
                option_selected=option_selected,
                correct=correct
            )
            question_completed.save()
            quiz_completed.questions_completed.add(question_completed)
        quiz_completed.save()
        user = MultiUser.objects.get(email=request.user.username)
        user.quiz_completed.add(quiz_completed)
        user.save()

        return redirect("index")
    return render(request, "pending_quiz.html", {"quiz": quiz})