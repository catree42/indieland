from django.db import models

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
    Publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name="publisher_game")
    Game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             related_name="publisher_game")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    reviews_num = models.IntegerField(default=0)
    review = models.CharField(max_length=20)
    review_score = models.DecimalField(null=True,
                                       max_digits=3,
                                       decimal_places=1)


class User(AbstractUser):
    login_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    played = models.ManyToManyField(
        Game,
        related_name="played_user",
        null=True,
        # through="UserGame",
        # through_fields=("user","game")
    )
    likes = models.ManyToManyField(
        Game,
        related_name="likes_user",
        null=True,
        # through="Likes",
        # through_fields=("user","game")
    )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.TextField(null=False, max_length=500)
    datetime = models.DateTimeField(auto_now=True)
