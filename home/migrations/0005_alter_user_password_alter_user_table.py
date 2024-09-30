# Generated by Django 5.1.1 on 2024-09-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_streamsite_alter_publishergame_game_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$870000$1zHo7J55Phx7xD2uJyFEzI$BLU0osDP5Bk1MyQhZmVZGpJHfvBSraRQgpEkXJicghM=",
                max_length=128,
            ),
        ),
        migrations.AlterModelTable(
            name="user",
            table="home_user",
        ),
    ]
