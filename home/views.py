from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import *
from home.serializers import *
from rest_framework import mixins, viewsets
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, "home/home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(
                "home")  # Redirect to home page on successful login
        else:
            messages.error(
                request,
                "Invalid username or password")  # Error message on failure
            return render(request, "home/login.html")  # Stay on the login page

    return render(request, "home/login.html")


def signup_view(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect("login")  # Redirect to login after sign-up
        else:
            # Pass detailed errors to the template
            return render(request, "home/signup.html",
                          {"errors": serializer.errors})

    return render(request, "home/signup.html")


def detail(request, pk):
    context =  get_object_or_404(Game, id = pk)
    return render(request, "home/<int:pk>.html", context)


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pass
