from django.db import models

# Create your models here.
class Batch(models.Model):
    url = models.CharField(max_length=255)
    batch_id = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    purchase_date = models.DateField() #datetime.datetime instance
    location = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    weight = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField()

class Cado(models.Model):
    url = models.CharField(max_length=255)
    batch_id = models.IntegerField()
    cado_id = models.IntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(decimal_places=2,max_digits=10)
    volume = models.DecimalField(decimal_places=2,max_digits=10)
    initial_color = models.CharField(max_length=255)
    initial_dense = models.DecimalField(decimal_places=2,max_digits=10)
    is_projected = models.BooleanField(default=False)
    
class Decline(models.Model):
    url = models.CharField(max_length=255)
    cado_id = models.IntegerField()
    date = models.DateTimeField()
    projected_dense = models.DecimalField(decimal_places=2,max_digits=10)