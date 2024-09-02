from django.contrib.admin import register, ModelAdmin
from .models import Customer

@register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ['user',
                    'is_owner'
    ]
