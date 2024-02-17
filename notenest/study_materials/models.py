from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('academic_info.Subject', on_delete=models.CASCADE)
    semester = models.IntegerField()
    material = models.FileField(upload_to='materials/')

    def __str__(self):
        return f"Material {self.material_id} - {self.subject} - Semester {self.semester}"
