from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Seat, Ticket
from .serializers import SeatSerializer, TicketSerializer

@api_view(['GET'])
def seat_list(request):
    seats= Seat.objects.all()
    serializer = SeatSerializer(seats, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_seat(request):
    serializer=SeatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
def ticket_list(request):
    tickets= Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_ticket(request):
    serializer=TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)