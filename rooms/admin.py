from django.contrib import admin
from .models import Room, Floor, Employee, WeekDay

# Register your models here.

admin.site.register(Room)
admin.site.register(Floor)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    filter_horizontal = ('work_days',)  # Удобный множественный выбор дней

@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('day',)