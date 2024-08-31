from django.db import models
from user.models import UserProfile



class Villa(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = 'owner')
    past_renters = models.ManyToManyField(UserProfile, related_name='renters', blank=True)
    current_renter = models.ForeignKey(UserProfile, on_delete= models.PROTECT, related_name='current_renter', blank=True, null=True)
    is_currently_rented = models.BooleanField(default=False)
    city = models.CharField(max_length=255)
    address = models.TextField()
    features = models.TextField()





