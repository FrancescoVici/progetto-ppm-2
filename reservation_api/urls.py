from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ReservationViewSet, UserListView, UserCreateView

router = DefaultRouter()
router.register(r'user', CustomUserViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/add/', UserCreateView.as_view(), name='user-add'),
]
