# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jwxt', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上传时间')),
                ('description', models.TextField()),
                ('questionfile', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Homeworkansower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上传时间')),
                ('description', models.TextField()),
                ('answerfile', models.FileField(upload_to='')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jwxt.Homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jwxt.Student')),
            ],
        ),
    ]