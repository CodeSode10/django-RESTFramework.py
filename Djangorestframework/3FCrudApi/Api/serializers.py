from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.salary = validated_data.get("salary", instance.salary)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance