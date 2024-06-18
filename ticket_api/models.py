from django.db import models

class Seat(models.Model):
    seat = models.IntegerField()
    row = models.IntegerField()

    def your_place(self):
        return self.seat + self.row
    

class Ticket(models.Model):
    event_id = models.IntegerField()
    seat_id = models.IntegerField()
    price = models. IntegerField()

    def __str__(self):
        return f"Ticket for {self.event_id} at {self.seat_id}"
    