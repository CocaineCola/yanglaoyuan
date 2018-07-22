# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_article_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='index',
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0, verbose_name='文章排序'),
        ),
    ]