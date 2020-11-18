from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuizTopic(models.Model):
    topic_name = models.CharField(max_length=20, null=False, blank=False)
    number_questions = models.IntegerField(null=False, blank=False)
    minimum_pass_count = models.IntegerField(null=False, blank=False)
    weightage_each_question = models.IntegerField(default=1, null=True, blank=True)


class UserQuiz(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    quiz_topic = models.ForeignKey(QuizTopic, null=False, blank=False, on_delete=models.CASCADE)
    number_of_answers_correct = models.IntegerField(null=False, blank=False)
    score = models.IntegerField(null=False, blank=True)
    is_pass = models.BooleanField(null=False, blank=True)

    def save(self, *args, **kwargs):
        self.score = self.number_of_answers_correct*self.quiz_topic.weightage_each_question
        if self.number_of_answers_correct >= self.quiz_topic.minimum_pass_count:
            self.is_pass = True
        else:
            self.is_pass = False
        return super().save(*args, **kwargs)


class Questions(models.Model):
    quiz_topic = models.ForeignKey(QuizTopic, null=False, blank=False, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250, null=False, blank=False)
    choice_one = models.CharField(max_length=50, null=False, blank=False)
    choice_two = models.CharField(max_length=50, null=False, blank=False)
    choice_three = models.CharField(max_length=50, null=False, blank=False)
    choice_four = models.CharField(max_length=50, null=False, blank=False)
    correct_answer = models.CharField(max_length=50, null=False, blank=False)
