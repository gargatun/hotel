from django.db import models

from rooms.models import Employee, Room

# Create your models here.
class CleaningSchedule(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.date} - {self.room} cleaned by {self.employee}"
