from django.shortcuts import render
from .serializers import VillaSerializer,RentSerializer,RateSerializer, CommentSerializer, VillaCreateSerializer
from .models import Villa , Comment , Rate, Rent
from rest_framework.generics import ( ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.models import Customer
from django.db import transaction
from owner.models import Owner
from django.utils.timezone import now
from datetime import timedelta
from django.http.response import JsonResponse
from rest_framework.exceptions import ValidationError
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from user.permissions import IsOwner, IsSuperUser


class VillaView(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
class VillaDetails(RetrieveAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer

class VillaCreateView(CreateAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        user = self.request.user

        try:
            customer = user.customer
        except Customer.DoesNotExist:
            raise PermissionError("You must be a customer to create a villa.")
        
        if not customer.is_owner :
            raise PermissionError("You must be an owner to create a villa.")
        
        owner =customer.owner
        serializer.save(owner=owner)
    
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

class RateCreatView(CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]

class CommentCreatView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class VillaCommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        villa_id = self.kwargs['villa_id']
        return Comment.objects.filter(villa_id = villa_id)

class VillaRateView(APIView):

    def get(self, request, villa_id):
        average_rate = Rate.objects.filter(villa_id=villa_id).aggregate(average=Avg('rate'))['average']

        return Response({'villa_id': villa_id, 'average_rate': average_rate})

class UpdateRentalStatus(APIView):
    permission_classes = [IsSuperUser]

    def post(self, request):
        current_time = now()

        expired_rentals = Rent.objects.filter(date_end__lt = current_time)
        for rental in expired_rentals:
            villa = rental.villa
            villa.is_currently_rented = False
            villa.save()

        return Response({"status" : "villas status has been updated"})

class OwnedVillasList(ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = VillaSerializer
    def get_queryset(self):
        user = self.request.user
        customer = user.customer
        if not customer.is_owner:
            raise PermissionError("You must be an owner to view this page.")
        owner = customer.owner
        return Villa.objects.filter(owner = owner)

            
            

