# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100)
    branch_id = models.ForeignKey('academic_info.Branch', on_delete=models.CASCADE)
    year = models.IntegerField()
    sem = models.IntegerField()

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tutor_id = models.CharField(max_length=100)
    subject_id = models.ForeignKey('academic_info.Subject', on_delete=models.CASCADE)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_id = models.CharField(max_length=100)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
