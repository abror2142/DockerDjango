from django.shortcuts import render
from rest_framework import viewsets

from .models import Follower, Message
from .serializers import FollowerSerializer, MessageSerializer


class FollowerAPIView(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    
    
class MessageAPIView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer