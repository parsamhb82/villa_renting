from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    money_wallet = models.IntegerField(default=0)
    is_owner = models.BooleanField(default= False)
    
    



    

    
