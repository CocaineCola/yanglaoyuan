# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20180609_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='award_id',
        ),
    ]
