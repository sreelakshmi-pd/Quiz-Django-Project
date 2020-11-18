# from django.shortcuts import render
from .models import (QuizTopic, UserQuiz, Questions, User)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .serializers import (QuizTopicSerializer,
                          UserQuizSerializer,
                          QuestionsSerializer,
                          UserSerializer)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view


class QuizTopicViewset(ModelViewSet):
    """
    Provides list, detail, create, update, delete for QuizTopic
    """
    queryset = QuizTopic.objects.all()
    serializer_class = QuizTopicSerializer


class UserQuizViewset(ModelViewSet):
    """
    Provides list, detail, create, update, delete for UserQuiz
    """
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer


class QuestionsViewset(ModelViewSet):
    """
    Provides list, detail, create, update, delete for Questions
    """
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class UserViewset(ModelViewSet):
    """
    Provides list, detail, create, update, delete for User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(), ]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            user_obj = User.objects.create_user(**data)
            return Response({
                "id": user_obj.id,
                "username": user_obj.username,
                "first_name": user_obj.first_name,
                "last_name": user_obj.last_name,
                "email": user_obj.email
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            pass
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuestionByQuizTopic(RetrieveAPIView):
    """
    Provedes retrieve by quic_topic id selected
    """
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    lookup_field = 'quiz_topic'
    lookup_table = Questions


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


@api_view(http_method_names=['GET'])
def log_out(request):
    token = Token.objects.filter(key=request.META['HTTP_AUTHORIZATION'].split()[1])
    if token:
        token.delete()
        return Response({"detail": "User logged out successfully"}, status=200)
    else:
        return Response({"error": "Invalid token"}, status=400)
