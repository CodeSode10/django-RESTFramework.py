from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def employeeApi(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_p_data = JSONParser().parse(stream)
        id = parsed_p_data.get("id", None)
        if id is not None:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return JsonResponse(serializer.data)
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_p_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=parsed_p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Message": "Data Created"}, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_p_data = JSONParser().parse(stream)
        id = parsed_p_data.get("id")
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=parsed_p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Message": "Data Updated"}, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_p_data = JSONParser().parse(stream)
        id = parsed_p_data.get("id")
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse({"Message": "Data Deleted"}, safe=False)
