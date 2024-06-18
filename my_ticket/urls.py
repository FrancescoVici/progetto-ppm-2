from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticket/', include('ticket_api.urls')),
    path('payment/', include('payment_api.urls'))
    # path('planning/', include('planning_api.urls')),
    # path('reservation/', include('reservation_api.urls'))
]
