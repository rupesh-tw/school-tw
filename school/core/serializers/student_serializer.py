from core.models import College, Teacher, Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'college', 'name', 'stream', 'teacher']
