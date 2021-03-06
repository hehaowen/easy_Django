# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('authors', models.ManyToManyField(to='author.Author')),
                ('publishers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.Publisher')),
            ],
        ),
    ]
