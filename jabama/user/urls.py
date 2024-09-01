
from django.urls import path
from . import views

urlpatterns = [
        path("create_owner/", views.CreateOwnerView.as_view())
]
