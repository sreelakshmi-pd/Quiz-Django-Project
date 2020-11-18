from django.contrib import admin
from .models import QuizTopic, Questions, UserQuiz


@admin.register(QuizTopic)
class QuizTopicAdmin(admin.ModelAdmin):
    model = QuizTopic
    list_display = ['pk', 'topic_name', 'number_questions', 'minimum_pass_count',
                    'weightage_each_question']


@admin.register(UserQuiz)
class UserQuizAdmin(admin.ModelAdmin):
    model = QuizTopic
    list_display = ['user', 'quiz_topic', 'number_of_answers_correct', 'score', 'is_pass']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    model = QuizTopic
    list_display = ['quiz_topic', 'question_text', 'choice_one',
                    'choice_two', 'choice_three', 'choice_four', 'correct_answer']
