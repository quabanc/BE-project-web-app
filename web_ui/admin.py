from django.contrib import admin
from .models import MultiUser, Option, Question, Quiz, Image, QuizCompleted, QuestionsCompleted
# Register your models here.

admin.site.register(MultiUser)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Image)
admin.site.register(QuizCompleted)
admin.site.register(QuestionsCompleted)