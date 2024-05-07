from django.contrib import admin
from .models import Guest, Booking
# from rooms.models import Room  # Это если вам нужно также управлять некоторыми аспектами номеров из админки бронирований


# Register your models here.
admin.site.register(Guest)
admin.site.register(Booking)
