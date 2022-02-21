from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
# Create your views here.d


class UserViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.  
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticated]   

class GroupViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.  
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer      
    permission_classes = [permissions.IsAuthenticated]