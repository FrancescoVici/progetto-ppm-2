from django.urls import path
from .views import PaymentCreateView, PaymentListView, method_list, create_method

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment-list'),
    path('add/', PaymentCreateView.as_view(), name='payment-create'),
    path('method/', method_list),
    path('method/add/', create_method)
]