from core.models import College
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'address', 'created_at']

