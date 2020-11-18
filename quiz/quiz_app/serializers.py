from .models import QuizTopic, UserQuiz, Questions, User
from rest_framework.serializers import ModelSerializer


class QuizTopicSerializer(ModelSerializer):
    class Meta:
        model = QuizTopic
        fields = '__all__'


class UserQuizSerializer(ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = '__all__'


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
