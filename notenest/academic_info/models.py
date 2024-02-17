# academic_info/models.py

from django.db import models

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    branch_duration = models.IntegerField()  # Duration in years

    def __str__(self):
        return self.branch_name

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    subject_duration = models.IntegerField()  # Duration in semesters

    def __str__(self):
        return self.subject_name

class Branch_subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('branch', 'subject')

class PrerequisiteSubject(models.Model):
    subject = models.ForeignKey(Subject, related_name='prerequisites', on_delete=models.CASCADE)
    prerequisite_subject = models.ForeignKey(Subject, related_name='required_for', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'prerequisite_subject')
