from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=100)