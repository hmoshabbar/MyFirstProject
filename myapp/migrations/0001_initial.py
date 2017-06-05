# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-01 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('createted_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]