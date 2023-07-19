# Generated by Django 4.2.2 on 2023-06-12 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_remove_playercontact_telephone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercontact',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Le format du téléphone n'est pas le bon...", regex='^\\+33\\d{9}$')]),
        ),
    ]