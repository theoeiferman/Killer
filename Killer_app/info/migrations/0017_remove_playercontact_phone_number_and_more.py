# Generated by Django 4.2.2 on 2023-06-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_playercontact_game_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playercontact',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='playercontact',
            name='player_email',
            field=models.EmailField(default='default_email@example.com', max_length=254, null=True),
        ),
    ]