from django.db import models
from .college_model import College
from .teacher_model import Teacher


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    stream = models.CharField(max_length=255)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'student_details'
        indexes = [
            models.Index(fields=['id'])
        ]