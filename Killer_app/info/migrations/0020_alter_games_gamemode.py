# Generated by Django 4.2.2 on 2023-07-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_remove_games_mode_games_gamemode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='gamemode',
            field=models.CharField(default='default', max_length=100),
        ),
    ]