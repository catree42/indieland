# Generated by Django 5.1.1 on 2024-09-24 06:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(to='home.tag'),
        ),
        migrations.AddField(
            model_name='game',
            name='youtube',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='likes_user', to='home.game'),
        ),
        migrations.AddField(
            model_name='user',
            name='played',
            field=models.ManyToManyField(related_name='played_user', to='home.game'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublisherGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('reviews_num', models.IntegerField(default=0)),
                ('review', models.CharField(max_length=20)),
                ('review_score', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game')),
                ('Publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.publisher')),
            ],
        ),
    ]
