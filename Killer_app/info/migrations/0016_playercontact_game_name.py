# Generated by Django 4.2.2 on 2023-06-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_remove_playercontact_game_games_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='playercontact',
            name='game_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
