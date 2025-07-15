from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model= Project
    fields= '__all__'

class TicketSerializer(serializers.ModelSerializer):
  class Meta:
    model= Ticket
    fields='__all__'