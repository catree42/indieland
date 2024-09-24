from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import *
from home.serializers import *
from rest_framework import mixins, viewsets

# Create your views here.


def home(request):
    return render(request,'home/home.html')

class GameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Game.objects.all().prefetch_related('publisher_game')
    serializer = PublichserGameSerializer(queryset, many=True)
        

