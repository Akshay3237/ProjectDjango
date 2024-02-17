# quiz_system/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('academic_info.Subject', on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField()

    def __str__(self):
        return f"Quiz {self.quiz_id} - {self.subject}"

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_definition = models.TextField()
    answer = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)

    def __str__(self):
        return f"Question {self.question_id} - {self.question_definition[:50]}..."

class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Result {self.result_id} - {self.student.username} - {self.quiz}"
