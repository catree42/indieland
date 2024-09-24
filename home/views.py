from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import *
from home.serializers import *
from rest_framework import viewsets

def home(request):

    return render(request,"home/home.html")
# Create your views here.

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()