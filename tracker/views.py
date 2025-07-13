from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import serializers
from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def get_view(request):
  resp=dict()
  resp["status_code"]=200
  resp["status_msg"]="get Api working"
  resp["some random key"]="random success value"
  resp["method type"]=str(request.method)
  return Response(resp)

@api_view(['GET', 'POST'])
def get_projects(request):
  if request.method=='GET':
    projects=Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)