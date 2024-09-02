from django.contrib.admin import register, ModelAdmin
from villa.models import Rate, Comment, Rent, Villa

@register(Villa)
class VillaAdmin(ModelAdmin):
    list_display = [
        'name',
        'owner'
        'is_currently_rented',
        'city',
    ]

@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = [
        'villa',
        'user',
        'comment',
    ]

@register(Rate)
class RateAdmin(ModelAdmin):
    list_display = [
        'villa',
        'user',
        'rate',
    ]

@register(Rent)
class RentAdmin(ModelAdmin):
    list_display = [
        'villa',
        'user',
        'date_start',
        'date_end',
        'date_created',
    ]
