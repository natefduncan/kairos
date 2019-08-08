from django.contrib.auth.models import User, Group
from rest_framework import viewset
from cado_django.rest_api.serializers import UserSerializer, GroupSerializer

from django.shortcuts import render #This was here by default.

class UserViewSet(viewset.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.object.all().order_by('-date-joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.object.all()
    serializer_class = GroupSerializer

