# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_of_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=33)),
            ],
        ),
        migrations.DeleteModel(
            name='listdo',
        ),
    ]
