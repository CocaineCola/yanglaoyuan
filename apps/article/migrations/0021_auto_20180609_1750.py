# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_remove_article_award'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='award',
            new_name='golden_spider_award',
        ),
    ]