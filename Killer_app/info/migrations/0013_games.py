# Generated by Django 4.2.2 on 2023-06-14 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_alter_playercontact_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Game0', max_length=30)),
                ('status', models.CharField(default='0', max_length=1)),
                ('started_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
