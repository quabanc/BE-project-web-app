from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    image = models.ImageField('img', upload_to='./web_ui/static/img/uploads')


class MultiUser(User):
    USER_TYPE_CHOICES = (
        ("STUDENT", "STUDENT"),
        ("TEACHER", "TEACHER")
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default="STUDENT")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email + " - " + self.user_type