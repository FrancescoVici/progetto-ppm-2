from django.urls import path
from .views import SeatListCreateView, SeatDetailView, TicketListCreateView, TicketDetailView

urlpatterns = [
    path('seats/', SeatListCreateView.as_view(), name='seat-list-create'),
    path('seats/<int:pk>/', SeatDetailView.as_view(), name='seat-detail'),
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]