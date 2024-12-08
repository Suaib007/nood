from django.urls import reverse
from django.http import JsonResponse
from rest_framework.test import APIClient

def use_fetch_orders(request):
    # Example order IDs
    order_ids = ["12345", "67890"]
    
    # Internal API call using reverse()
    url = reverse('fetch_orders')  # URL name defined in nood-api/urls.py
    client = APIClient()
    response = client.post(url, {"orderIds": order_ids}, format='json')
    
    return JsonResponse(response.data)






