from django.urls import path
from villa.views import (VillaView,
                        VillaDetails,
                        VillaCreateView,
                        CreatRentVilla,
                        RateCreatView,
                        CommentCreatView,
                        VillaCommentListView,
                        VillaRateView,
                        UpdateRentalStatus,
                        OwnedVillasList)

urlpatterns = [
    path('villas/', VillaView.as_view(), name='villa-list'),  # List all villas
    path('villas/<int:pk>/', VillaDetails.as_view(), name='villa-detail'),  # Details of a single villa
    path('villas/create/', VillaCreateView.as_view(), name='villa-create'),  # Create a new villa
    path('rents/create/', CreatRentVilla.as_view(), name='rent-create'),  # Create a new rent record
    path('rates/create/', RateCreatView.as_view(), name='rate-create'),  # Create a new rate record
    path('comments/create/', CommentCreatView.as_view(), name='comment-create'),  # Create a new comment
    path('villas/<int:villa_id>/comments/', VillaCommentListView.as_view(), name='villa-comments'),  # List comments for a villa
    path('villas/<int:villa_id>/rate/', VillaRateView.as_view(), name='villa-rate'),  # Get average rate for a villa
    path('rents/update-status/', UpdateRentalStatus.as_view(), name='update-rental-status'),  # Update rental status of villas
    path('villas/owned/', OwnedVillasList.as_view(), name='owned-villas'),  # List all villas owned by the logged in user
]
