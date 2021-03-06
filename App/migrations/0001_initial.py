# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('uname', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('img', models.ImageField(default='static/img/default.png', upload_to='static/img')),
            ],
        ),
    ]
