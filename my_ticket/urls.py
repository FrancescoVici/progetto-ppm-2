from django.contrib import admin
from django.urls import path,include
from .views import main_view


urlpatterns = [
   path('', main_view, name='index'),
    path('ticket/', include('ticket_api.urls')),
    path('pay/', include('payment_api.urls')),
    path('plan/', include('planning_api.urls')),
    path('buy/', include('reservation_api.urls'))
    
]
