from django.urls import path
from .views import fetch_orders

urlpatterns = [
    path('fetchOrders/', fetch_orders, name='fetch_orders'),
]
