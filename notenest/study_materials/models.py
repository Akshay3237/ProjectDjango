from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Material(models.Model):
    MATERIAL_TYPES = [
        ('p', 'Paper'),
        ('n', 'Notes'),
    ]
    material_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey('academic_info.Subject', on_delete=models.CASCADE)
    material = models.FileField(upload_to='materials/')
    year = models.IntegerField()
    material_type = models.CharField(max_length=1, choices=MATERIAL_TYPES)
    aproved=models.BooleanField(default=False)
    def __str__(self):
        return f"Material {self.material_id} - {self.subject}"