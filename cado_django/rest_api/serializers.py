from django.contrib.auth.models import User, Group
from .models import Batch, Cado, Decline
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ['url', 'upload_date', 'purchase_date','location', 'provider', 'cost', 'weight', 'quantity']

class CadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cado
        fields = ['url', 'batch_id', 'cado_id', 'weight', 'volume', 'initial_color', 'initial_dense']

class DeclineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decline
        fields = ['url', 'cado_id', 'date', 'projected_dense']

