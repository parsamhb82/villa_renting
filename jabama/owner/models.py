from django.db import models
from user.models import Customer

class Owner(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='owner')

    def __str__(self) -> str:
        return f'{self.customer.user.username} owner model'

    
    
    