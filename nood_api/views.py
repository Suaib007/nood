from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['POST'])
def fetch_orders(request):
   # return Response({"message": "Welcome to the fetchOrders API!"}, status=200)
   
    try:
        # Extract the list of order IDs from the request body
        order_ids = request.data.get('orderIds', [])
        
        if not order_ids or not isinstance(order_ids, list):
            return Response({"error": "Invalid request body. 'orderIds' must be a list of strings."}, status=400)

        # Shipmonk API details
        base_url = "https://api.shipmonk.com"
        api_endpoint = "/v1/integrations/orders"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Api-Key": "prod_RlkL6Hjx8ZJBzocKv6EN4HOKyaSSJPeCHjJyt5HhqWOfXFMjYe"
        }

        # Initialize the response container
        responses = {}

        # Fetch details for each order ID
        for order_id in order_ids:
            api_url = f"{base_url}{api_endpoint}?orderKey={order_id}"
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200:
                responses[order_id] = response.json()  # Successful response
            else:
                responses[order_id] = {
                    "error": f"Failed to fetch details for order ID {order_id}.",
                    "status_code": response.status_code,
                    "message": response.text
                }

        return Response(responses, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
