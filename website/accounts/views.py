from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileAPIView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
