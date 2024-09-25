from django.http import Http404
from django.shortcuts import render, get_object_or_404
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


def detail(request, pk):
    context =  get_object_or_404(Game, id = pk)
    return render(request, "home/<int:pk>.html", context)


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pass
