# Generated by Django 4.2.2 on 2023-06-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_player_date_created_player_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
