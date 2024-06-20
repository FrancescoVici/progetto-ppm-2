from django.shortcuts import render

from rest_framework import viewsets
from .models import CustomUser, Reservation
from .serializers import CustomUserSerializer, ReservationSerializer
from django.views.generic import TemplateView

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserListView(TemplateView):
    template_name = 'user_list.html'

class UserCreateView(TemplateView):
    template_name = 'user_form.html'