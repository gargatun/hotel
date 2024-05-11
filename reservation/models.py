from django.db import models
from django.forms import ValidationError
from rooms.models import Room

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", default='')
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", default='')
    passport_number = models.CharField(max_length=20, verbose_name="Номер паспорта")
    city_from = models.CharField(max_length=100, verbose_name="Город прибытия")
    guest_number = models.CharField(max_length=20, verbose_name="Номер гостя", null=True, blank=True)


    def __str__(self):
        return f"Гость {self.first_name} {self.last_name}"
    
	
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name="Номер")
    check_in = models.DateField(verbose_name="Дата заезда")
    check_out = models.DateField(verbose_name="Дата выезда")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings', verbose_name="Гость")
    full_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Полная стоимость", null=True)
    is_paid = models.BooleanField(default=False, verbose_name="Статус платежа")

    def __str__(self):
        return f"Бронирование {self.id} - {self.room}"
    
    def clean(self):
        if self.check_in >= self.check_out:
            raise ValidationError("Check-out date must be after check-in date.")

    def save(self, *args, **kwargs):
        # Calculate the duration of the stay
        duration = (self.check_out - self.check_in).days
        if duration <= 0:
            duration = 1  # Ensures that even one day stays are calculated correctly

        # Calculate full price based on the room's price per night
        self.full_price = self.room.price * duration
        super().save(*args, **kwargs)