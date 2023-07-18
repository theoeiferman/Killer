# Generated by Django 4.2.2 on 2023-07-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_remove_games_status_games_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='mode',
        ),
        migrations.AddField(
            model_name='games',
            name='gamemode',
            field=models.CharField(default='defa', max_length=100),
        ),
    ]
