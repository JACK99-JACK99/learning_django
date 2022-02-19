from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import Viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
# Create your views here.


class UserViewset(Viewsets.ModalViewSet):
    """
    API endpoint that allows users to be viewed or edited.  
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAuthenticated]   

class GroupViewset(Viewsets.ModalviewSet):
    """
    API endpoint that allows users to be viewed or edited.  
    """
    query = Group.objects.all()
    serializer_class = GroupSerializer      
    permission_classes = [permissions.IsAutheticated]