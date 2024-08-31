from django.db import models
from user.models import Customer
# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(Customer)
    
    