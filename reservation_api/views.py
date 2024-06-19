from django.shortcuts import render

from rest_framework import viewsets
from .models import CustomUser, Reservation
from .serializers import CustomUserSerializer, ReservationSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
