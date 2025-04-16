from django.urls import path
from fuelroute.views import fuel_route

urlpatterns = [
    path('fuel-route/', fuel_route, name='fuel_route'),
]
