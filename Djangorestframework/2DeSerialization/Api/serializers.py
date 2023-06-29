from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)