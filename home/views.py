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
from django.db.models import Value, OuterRef, Subquery
from django.db.models.functions import Coalesce



# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignupSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def recommend(request):
    if request.method == "GET":
        games = Game.objects.all()
        return render(request, "home/recommend.html", {"games": games})
    elif request.method == "POST":
        if "tags" in request.POST:
            keys = request.POST.getlist("tags")
            print(keys)
            game_dict = {
                '액션': 1,
                '퍼즐': 2,
                '리듬': 3,
                '디펜스': 4,
                '비주얼 노벨': 5,
                'RPG': 6,
                '전략': 7,
                '어드벤처': 8,
                '캐주얼': 9,
                '시뮬레이션': 10,
                '플랫포머': 11,
                '슈팅': 12,
                '공포': 13,
                '기능성 게임': 14,
                '기타': 15
            }
            tids = [game_dict[x] for x in keys]
            print(tids)
            games = Game.objects.filter(tags__in=tids)
            return render(request, "home/recommend.html", {"games": games})
        else:
            print("no tags")
            games = Game.objects.all()
            return render(request, "home/recommend.html", {"games": games})



class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    def get(self, request, *args, **kwargs):
        return render(request, 'home/login.html') 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
class UserSignupView(generics.GenericAPIView):
    serializer_class = UserSignupSerializer
    def get(self, request, *args, **kwargs):
        return render(request, 'home/signup.html') 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)  # JWT 토큰 생성
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': '회원가입 성공!'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home_view(request):
    sort_by = request.GET.get('sort', 'reviews_num')  # 기본값은 'reviews_num'

    # StreamGame에서 viewers_num을 가져오기 위한 서브쿼리
    viewers_subquery = StreamGame.objects.filter(game=OuterRef('game')).values('viewers_num')[:1]

    if sort_by == 'viewers_num':
        publisher_games = PublisherGame.objects.annotate(
            viewers_num=Coalesce(Subquery(viewers_subquery), Value(0))  # viewers_num이 null인 경우 0으로 대체
        ).order_by('-viewers_num')
    elif sort_by == 'review_score':
        publisher_games = PublisherGame.objects.all().order_by('-review_score')
    else:  # 기본적으로 리뷰 수로 정렬
        publisher_games = PublisherGame.objects.all().order_by('-reviews_num')

    print(publisher_games[0].game.id)
    return render(request, 'home/home.html', {'publisher_games': publisher_games})

#====================================================================================================================

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
from django.shortcuts import  redirect, render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Game, Comment, User
from .forms import CommentForm
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote
# Create your views here.

def detail(request, pk):
    game = get_object_or_404(Game, id=pk)
    pbid = get_object_or_404(PublisherGame, id = pk)
    user = request.user
    user_liked = game.likes_user.filter(id=request.user.id).exists()
    likes_count = game.likes_user.count()
    gametxt = Game.objects.get(id = pk)
    pbtxt = PublisherGame.objects.get(id = pk)
    Comments = game.comment_game.all()
    new_comment = None
    GameCommentList = GameComment.objects.filter(publisher_game_id=pk)
    game_title = quote(game.name)
    print(game_title)
    print(pbid.publisher_id)
    if pbid.publisher_id == 1:
        url = f'https://store.steampowered.com/search/?term={game_title}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            productlist = soup.select_one('#search_resultsRows > a:nth-child(1)')
            if productlist:
                href = productlist['href']
            else:
                href = None
        else:
            href = None
    else:
        headers = {
            "Referer": "https://store.onstove.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Origin": "https://store.onstove.com",
            "x-api-version": "v3",
            "x-client-lang": "ko",
            "x-device-type": "P01",
            "x-lang": "ko",
            "x-nation": "KR",
            "x-timezone": "Asia/Seoul",
            "x-utc-offset": "540",
            "x-uuid": "c0617e2a-2eeb-4391-ad50-41ac4a831098"}
        print(game_title)
        url = f"https://api.onstove.com/indie-game/products/search?q={game_title}&currency_code=KRW&page=1&size=36&direction=SCORE&rating.board=GRAC&tag_aggregation_size=6&genre_aggregation_size=6&timestemp=1727431850474"
        print(url)
        with requests.Session() as session:
            session.headers.update(headers)
            resp = session.get(url)
            if resp.status_code == 200:
                body = resp.json()
                with open('stove_games.json', 'w', encoding='utf-8') as f:
                    json.dump(body, f, ensure_ascii=False)
                    print(f"성공")
            else:
                print(f"오류 발생: {resp.status_code}")
            product_no = body['value']['contents'][0]['product_no']
            print(product_no)
            href = f'https://store.onstove.com/ko/games/{product_no}'
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.game = game
            new_comment.user = request.user
            new_comment.save()
            return redirect('detail', pk = pk)
    else:
        comment_form = CommentForm()
    context = {
        'gametxt' : gametxt,
        'pbtxt' : pbtxt,
        'game': game,
        'comments': Comments,
        'comment_form': comment_form,
        'user_liked': user_liked,
        'likes_count': likes_count,
        'gamecomments': GameCommentList,
        'href':href,
    }
    return render(request, "home/detail.html", context)
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect('detail', pk=comment.game_id)
@login_required
def likegame(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.user.likes.filter(id=game.id).exists():
        request.user.likes.remove(game)
    else:
        request.user.likes.add(game)
    return redirect('detail', pk=game.id)
