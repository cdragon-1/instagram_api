# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postphoto_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pk',)},
        ),
    ]
