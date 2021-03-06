# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-09-10 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prispevok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obsah', models.CharField(max_length=10000)),
                ('vznikol', models.DateTimeField(auto_now_add=True)),
                ('uzivatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prispevky', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
