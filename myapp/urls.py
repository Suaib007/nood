from django.urls import path
from .views import dummy_api

urlpatterns = [
    path('dummy-api/', dummy_api, name='dummy_api'),
]
