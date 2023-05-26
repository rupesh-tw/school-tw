from django.db import models
from .college_model import College



class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'teacher_details'
        indexes = [
            models.Index(fields=['id'])
        ]