from core.models import College, Teacher, Student
from rest_framework import serializers


class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'college', 'name', 'stream', 'teacher']

    # def validate(self, attrs):
    #    breakpoint()


class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'college', 'name', 'stream', 'teacher']
        depth = 1
