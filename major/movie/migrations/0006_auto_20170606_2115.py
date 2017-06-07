# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc
import movie.models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20170603_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='movie',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=movie.models.uploadPhoto),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2017, 6, 6, 15, 30, 6, 205223, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
