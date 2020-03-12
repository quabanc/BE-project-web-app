from django.contrib import admin
from .models import MultiUser, Option, Question, Quiz, Image
# Register your models here.

admin.site.register(MultiUser)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Image)