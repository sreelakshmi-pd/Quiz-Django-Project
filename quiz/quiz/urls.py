"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz_app.views import (QuizTopicViewset,
                            UserQuizViewset,
                            QuestionsViewset,
                            UserViewset,
                            QuestionByQuizTopic,
                            log_out)
from quiz_app.views import CustomObtainAuthToken


router = DefaultRouter()
router.register(r'quiz_topic', QuizTopicViewset)
router.register(r'user_quiz', UserQuizViewset)
router.register(r'questions', QuestionsViewset)
router.register(r'user', UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'v1/', include(router.urls)),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('logout', log_out),
    path('questions_by_quiz_topic_id/<quiz_topic>', QuestionByQuizTopic.as_view())
]
