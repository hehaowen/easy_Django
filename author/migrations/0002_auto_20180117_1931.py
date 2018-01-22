# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='aut_name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='hometown',
            field=models.CharField(max_length=100, verbose_name='家乡'),
        ),
    ]