# from django.urls import path
# from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path("login/", views.UserLoginView.as_view(), name="login"),
#     path("api/token/", views.UserLoginView.as_view(), name="token_obtain_pair"),
#     path("<int:pk>", views.detail, name="detail"),
#     path("recommend/", views.recommend, name='recommend'),
#     path("signup/", views.UserSignupView.as_view(), name="signup"),
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
#     path("detail/<int:pk>/", views.detail, name = "detail"),
#     path('detail/<int:game_id>/like/', views.likegame, name='like_game'),
#     path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
# ]

from django.urls import path
from .views import UserLoginView, UserSignupView, home_view, detail, recommend, likegame, delete_comment
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', home_view, name='home'),
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/", UserSignupView.as_view(), name="signup"),
    
    # JWT 토큰 관련 URL
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path("<int:pk>/", detail, name="detail"),
    path("recommend/", recommend, name='recommend'),
    path('detail/<int:game_id>/like/', likegame, name='like_game'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
