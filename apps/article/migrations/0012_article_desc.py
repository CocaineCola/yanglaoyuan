# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20180512_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.CharField(blank=True, max_length=100, verbose_name='文章摘要'),
        ),
    ]