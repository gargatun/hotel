from django.db import models


# Create your models here.

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Одноместный'),
        ('double', 'Двухместный'),
        ('triple', 'Трехместный'),
    )
    name = models.CharField(max_length=255, verbose_name="Название номера", null=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name="Тип номера")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость за ночь")
    floor = models.IntegerField(verbose_name="Этаж")
    is_available = models.BooleanField(default=True, verbose_name="Доступность")
    image = models.ImageField(upload_to='room_images/', verbose_name="Изображение", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True)


    def __str__(self):
        return f"{self.name} - {self.get_room_type_display()} на этаже {self.floor}"



class Floor(models.Model):
    number = models.IntegerField(verbose_name="Номер этажа")

    def __str__(self):
        return f"Этаж {self.number}"
    
class WeekDay(models.Model):
    DAY_CHOICES = (
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    )
    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True, verbose_name="День недели")

    def __str__(self):
        return self.get_day_display()
    


class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    floors = models.ManyToManyField('Floor', related_name='employees', verbose_name="Этажи")
    work_days = models.ManyToManyField(WeekDay, verbose_name="Дни работы")

    def __str__(self):
        return self.full_name