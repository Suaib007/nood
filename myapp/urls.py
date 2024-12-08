from django.urls import path
from .views import use_fetch_orders

urlpatterns = [
    path('use_fetch_orders/',use_fetch_orders, name='use_fetch_orders')
   
]
