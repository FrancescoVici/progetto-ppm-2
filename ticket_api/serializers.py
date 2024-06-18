from rest_framework import serializers
from .models import Seat,Ticket

class SeatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Seat
        fields = ['id','seat','row']

    def create(self,data):
        return Seat.objects.create(**data)



class TicketSerializer(serializers.ModelSerializer):
    seat = SeatSerializer(read_only=True)
    seat_id = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all(), source='seat', write_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'seat', 'seat_id', 'price', 'event']