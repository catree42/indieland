# Generated by Django 4.2.16 on 2024-09-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='youtube',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$DsFvBYdf93s1bXBYxC5FL6$KQ9jUl17ik9xFAE2zy/49RfPfVj/4G9Y6qCzqwg7o4s=', max_length=128),
        ),
    ]
