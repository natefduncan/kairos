from django.contrib.auth.models import User, Group
from .models import Batch, Cado, Decline
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, BatchSerializer, CadoSerializer, DeclineSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that houses all data on batches
    """
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class CadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that houses all data on avocado
    """
    queryset = Cado.objects.all()
    serializer_class = CadoSerializer

class DeclineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that houses all data on avocado decline curves. 
    """
    queryset = Decline.objects.all()
    serializer_class = DeclineSerializer
    
