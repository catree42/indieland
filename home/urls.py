from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('', views.home_view, name='home'),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("api/token/", views.UserLoginView.as_view(), name="token_obtain_pair"),
    path("<int:pk>", views.detail, name="detail"),
    path("recommend/", views.recommend, name='recommend'),
    path("signup/", views.UserSignupView.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("detail/<int:pk>/", views.detail, name = "detail"),
    path('detail/<int:game_id>/like/', views.likegame, name='like_game'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
