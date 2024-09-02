from django.contrib.admin import register, ModelAdmin
from .models import Owner
@register(Owner)
class OwnerAdmin(ModelAdmin):
    list_display = ['customer']

