from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

# Create your views here.

@api_view(['GET', 'POST'])
def get_view(request):
  resp=dict()
  resp["status_code"]=200
  resp["status_msg"]="get Api working"
  resp["some random key"]="random success value"
  resp["method type"]=str(request.method)
  return Response(resp)

@api_view(['GET'])
def get_projects(request):
  if request.method=='GET':
    projects=Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
  
@api_view(['POST'])
def add_project(request):
  data=request.data
  serializer=ProjectSerializer(data=data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response({"msg": "cant save project"})

@api_view(['PUT', 'PATCH'])
def update_project(request):
  if request.method=='PUT':
    data=request.data
    project=Project.objects.get(id=data['id'])
    serializer=ProjectSerializer(project, data=data, partial=False)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)
  elif request.method=='PATCH':
    data=request.data
    project=Project.objects.get(id=data['id'])
    serializer=ProjectSerializer(project, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)
  else:
    return Response({"msg": "error"})

@api_view(['DELETE'])
def delete_project(request):
  data=request.data
  obj=get_object_or_404(Project, id=data['id'])
  obj.delete()
  return Response({"msg": "deleted"})


# Ticket methods

@api_view(['GET'])
def get_all_tickets(request):
  tickets=Ticket.objects.all()
  serializer=TicketSerializer(tickets, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_ticket(request):
  data=request.data
  serializer=TicketSerializer(data=data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response({"msg":"couldn't save ticket"})


@api_view(['GET', 'PUT', 'PATCH'])
def ticket(request, id):
  ticket=get_object_or_404(Ticket, id=id)
  if request.method=='GET':
    serializer=TicketSerializer(ticket)
    return Response(serializer.data)
  else:
    data=request.data
    serializer=None
    if request.method=='PUT':
      serializer=TicketSerializer(ticket, data=data)  
    elif request.method=='PATCH':
      serializer=TicketSerializer(ticket, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, HTTP_200_OK)
    return Response(serializer.errors, HTTP_404_NOT_FOUND)
  

@api_view(['GET'])
def tickets_based_on_project(request, project_id):
  tickets=Ticket.objects.filter(project_id=project_id)
  serializer=TicketSerializer(tickets, many=True)
  return Response(serializer.data)