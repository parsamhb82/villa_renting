from django.db import models
from user.models import Customer

class Owner(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='owner')

    
    
    