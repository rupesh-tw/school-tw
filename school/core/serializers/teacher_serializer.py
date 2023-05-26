from core.models import College, Teacher
from rest_framework import serializers


class TeacherCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'college', 'name', 'subject']


class TeacherGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'college', 'name', 'subject']
        depth = 1
