from .models import Batch, Cado, Decline, CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']
        
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batch_id', 'upload_date', 'purchase_date','location', 'provider', 'cost', 'weight', 'quantity']

class CadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cado
        fields = ['batch_id', 'cado_id', 'weight', 'volume', 'initial_color', 'initial_dense']

class DeclineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decline
        fields = ['decline_id', 'cado_id', 'date', 'projected_dense']

