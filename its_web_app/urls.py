"""its_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_ui.views import (index_view, profile_view, login_view, logout_view,
                          register_view, quiz_view, created_quiz_view, uploaded_quiz, 
                          pending_quiz, completed_quiz)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('profile/', profile_view, name="profile"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('quiz/', quiz_view, name="quiz"),
    path('created_quiz/', created_quiz_view, name="created_quiz"),
    path('uploaded_quiz/<str:quiz_name>/', uploaded_quiz, name="uploaded_quiz"),
    path('pending_quiz/<str:quiz_name>/', pending_quiz, name="pending_quiz"),
    path('completed_quiz/<str:quiz_name>/', completed_quiz, name="completed_quiz"),
]
