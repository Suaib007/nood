from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def dummy_api(request):
    data = {
        "status": "success",
        "message": "This is a dummy API return data in json format ",
        "data": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "Mrblackjhondoe@"
        }
    }
    return JsonResponse(data)
