from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sport
from .serializers import SportSerializer

# Create your views here.

class SportList(APIView):
    def get (self, request):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports,many = True)
        return Response(serializer.data)
    def post (self, request):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports,many = True)
        return Response(serializer.data)

def index(request):
    return HttpResponse("<h1>test</h1>")

def test(request):
    return HttpResponse("<h1>aaa</h1>")
