from django.db import models
from planning_api.models import Planning

class Seat(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()

    def your_place(self):
        return f"Row {self.row}, Seat {self.seat}"

    def __str__(self):
        return f"Row {self.row}, Seat {self.seat}"

class Ticket(models.Model):
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='tickets', default=1)
    
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket for {self.planning.event.name} at {self.seat}"


    