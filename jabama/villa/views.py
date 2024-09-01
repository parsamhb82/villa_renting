from django.shortcuts import render
from .serializers import VillaSerializer,RentSerializer,RateSerializer, CommentSerializer
from .models import Villa , Comment , Rate, Rent
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.models import Customer
from django.db import transaction
from owner.models import Owner
from django.utils.timezone import now
from datetime import timedelta
from django.http.response import JsonResponse
from rest_framework.exceptions import ValidationError



class VillaView(ListAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
class VillaDetails(RetrieveAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer

class VillaCreateView(CreateAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    permission_classes = [IsAuthenticated]
    
class CreatRentVilla(CreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        customer = user.customer
        villa = serializer.validated_data['villa']
        date_start = serializer.validated_data['date_start']
        date_end = serializer.validated_data['date_end']
        if date_end <= date_start:
            raise ValidationError("The end date must be after the start date.")
        num_days = (date_end - date_start).days
        total_cost = num_days * villa.price
        if customer.money_wallet < total_cost:
            raise ValidationError("You don't have enough money to rent this villa for the selected period.")
        with transaction.atomic():
            customer.money_wallet -= total_cost
            villa.owner.customer.money_wallet += total_cost
            villa.is_currently_rented = True
            villa.save()

            serializer.save(user = customer, villa = villa, date_start = date_start, date_end = date_end, date_created = now())
            
            

