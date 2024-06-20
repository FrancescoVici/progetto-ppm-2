from django.urls import path
from .views import EventListAPIView, EventDetailView, LocationListCreateView, LocationDetailView, PlanningListCreateView, PlanningDetailView, create_planning, delete_planning, planning_form_view

urlpatterns = [    
    path('', PlanningListCreateView.as_view(), name='planning-list-create'),
    path('<int:pk>/', PlanningDetailView.as_view(), name='planning-detail'),
    path('form/', planning_form_view, name='planning-form'),
    path('create/', create_planning, name='planning-create'),
    path('delete/<int:pk>/', delete_planning, name='planning-delete'),
    path('events/', EventListAPIView.as_view(), name='events_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail')
    
]