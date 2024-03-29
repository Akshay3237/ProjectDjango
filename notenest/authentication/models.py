# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USERTYPE_CHOICES = [
        ('s', 'Student'),
        ('t', 'Teacher'),
        ('p', 'Parent'),
    ]
    usertype = models.CharField(max_length=1, choices=USERTYPE_CHOICES)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch_id = models.ForeignKey('academic_info.Branch', on_delete=models.CASCADE)
    year = models.IntegerField()
    sem = models.IntegerField()
    def _str_(self):
            return f"{self.user.username} (Year: {self.year}, Semester: {self.sem})"

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey('academic_info.Subject', on_delete=models.CASCADE)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)