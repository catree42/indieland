from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Publisher(models.Model):
    name = models.CharField(max_length=30)


class Game(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    youtube = models.URLField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name="tag_game")


class PublisherGame(models.Model):
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name="publisher_game",
                                  null=True)
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             related_name="publisher_game",
                             null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    reviews_num = models.IntegerField(default=0)
    review = models.CharField(max_length=20)
    review_score = models.DecimalField(null=True,
                                       max_digits=3,
                                       decimal_places=1)


class GameComment(models.Model):
    publisher_game = models.ForeignKey(PublisherGame,
                                       on_delete=models.CASCADE,
                                       related_name="pg_comment")
    datetime = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=400)


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(
        max_length=128, default=make_password(
            "default_password"))  # Explicitly included, matching AbstractUser
    email = models.EmailField(max_length=254, unique=True)
    nickname = models.CharField(max_length=30)
    played = models.ManyToManyField(
        "Game",
        related_name="played_user",
        blank=True,
    )
    likes = models.ManyToManyField(
        "Game",
        related_name="likes_user",
        blank=True,
    )
    email = models.CharField(max_length=50)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nickname"]

    class Meta:
        db_table = "home_user"  # Use the same table name as the default User model

    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.TextField(null=False, max_length=500)
    datetime = models.DateTimeField(auto_now=True)


class StreamSite(models.Model):
    name = models.CharField(max_length=20)


class StreamGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stream = models.ForeignKey(StreamSite, on_delete=models.CASCADE)
    viewers_num = models.IntegerField(default=0)
