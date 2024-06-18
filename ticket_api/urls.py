from django.urls import path
from .views import seat_list, create_seat, ticket_list, create_ticket

urlpatterns = [
    path('', ticket_list),
    path('add/', create_ticket),
    path('seat/', seat_list),
    path('seat/add/', create_seat)
]