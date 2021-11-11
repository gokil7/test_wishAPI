from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Birthday
from .serializers import BirthdaySerializer
# import requests

@api_view(['POST'])
def wishApi(request):
    # url = "https://hooks.zapier.com/hooks/catch/11240506/bdood4m/silent/"
    # r = requests.get(url)
    serializer = BirthdaySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    resp = serializer.data

    print(resp['name'])

    str = "Happy Birthday," + resp['name']

    wish_str  = {
        'wish' : str
    }
    return Response(wish_str)