# Generated by Django 4.2.2 on 2023-06-11 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_playercontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='playercontact',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]