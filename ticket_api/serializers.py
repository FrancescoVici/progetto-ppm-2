from rest_framework import serializers
from .models import Seat, Ticket
from planning_api.models import Planning

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    planning = serializers.PrimaryKeyRelatedField(queryset=Planning.objects.all())
    seat = SeatSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        seat_data = validated_data.pop('seat')
        seat = Seat.objects.create(**seat_data)
        ticket = Ticket.objects.create(seat=seat, **validated_data)
        return ticket
