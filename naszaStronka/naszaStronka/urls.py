from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('naszaAplikacja/', include('naszaAplikacja.urls')),
    path('admin/', admin.site.urls),
    path('naszaAplikacja/zlecenia', include('rest_framework.urls')),
    path('naszaAplikacja/ciezarowki', include('rest_framework.urls')),
    path('naszaAplikacja/kierowca', include('rest_framework.urls')),
]
