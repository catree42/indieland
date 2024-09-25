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

<<<<<<< HEAD
def index(request):
    return render(request, 'index/index.html')

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pass
=======
class GameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Game.objects.all().prefetch_related('publisher_game')
    serializer = PublichserGameSerializer(queryset, many=True)
        
>>>>>>> 84273a8a1be5ccb6a034925fb41b83bb66a74574

