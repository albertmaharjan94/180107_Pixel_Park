# Generated by Django 3.0 on 2020-02-01 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_park_django', '0002_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
