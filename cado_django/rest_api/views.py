#Base imports
from .models import Batch, Cado, Decline, CustomUser
from .serializers import BatchSerializer, CadoSerializer, DeclineSerializer, CustomUserSerializer

#Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


#Model View Sets
class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer

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
    
