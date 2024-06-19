# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet, ReservationViewSet

# router = DefaultRouter()
# router.register(r'users', CustomUserViewSet)
# router.register(r'reservation_api', ReservationViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'user', CustomUserViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]