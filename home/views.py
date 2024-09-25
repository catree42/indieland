from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import *
from home.serializers import *
from rest_framework import mixins, viewsets

# Create your views here.


def home(request):
    return render(request, "home/home.html")


def login(request):
    return render(request, "home/login.html")


def signup(request):
    return render(request, "home/signup.html")


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pass
