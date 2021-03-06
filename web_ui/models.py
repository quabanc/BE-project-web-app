from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    image = models.ImageField('img', upload_to='./web_ui/static/img/uploads')


class Option(models.Model):
    option = models.TextField(blank=False)
    correct = models.BooleanField(blank=False)

    def __str__(self):
        return self.option


class Question(models.Model):
    image = models.TextField(blank=False)
    caption = models.TextField(blank=False)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.caption


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=250, unique=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.quiz_name


class QuestionsCompleted(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_selected = models.TextField(blank=False)
    correct = models.BooleanField(blank=False)

    def __str__(self):
        return self.question.caption


class QuizCompleted(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questions_completed = models.ManyToManyField(QuestionsCompleted, blank=True)

    def __str__(self):
        return self.quiz.quiz_name


class MultiUser(User):
    USER_TYPE_CHOICES = (
        ("STUDENT", "STUDENT"),
        ("TEACHER", "TEACHER")
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default="STUDENT")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # For Students Only.
    quiz_completed = models.ManyToManyField(QuizCompleted, blank=True)

    def __str__(self):
        return self.email + " - " + self.user_type