from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def createEmployee(requset):
    if requset.method=="POST":
        json_data = requset.body
        stream = io.BytesIO(json_data)
        parsed_p_data = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=parsed_p_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'Message':'Data Created'}, safe=False)
