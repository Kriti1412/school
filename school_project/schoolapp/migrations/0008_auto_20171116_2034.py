# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0007_auto_20171116_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
