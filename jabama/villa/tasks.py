from celery import shared_task
from .models import Villa, Rent
from datetime import datetime
from django.utils import timezone
from rest_framework.response import Response

@shared_task(bind = True, default_retry_delay = 300)
def update_rental_status(self, current_time):
    try:
        expired_rentals = Rent.objects.filter(date_end__lt = current_time)
        for rental in expired_rentals:
            villa = rental.villa
            villa.is_currently_rented = False
            villa.save()

        return Response({"status" : "villas status has been updated"})
    except Exception as e:
        return self.retry(exc=e,max_retries=10)

    