from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def employees(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def employee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
