# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwxt', '0005_homework_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkansower',
            name='description',
        ),
    ]
