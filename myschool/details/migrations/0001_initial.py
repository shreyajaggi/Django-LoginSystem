# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_S', models.CharField(max_length=50)),
                ('emails_S', models.EmailField(max_length=254)),
                ('rollnumber', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.cl')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_T', models.CharField(max_length=50)),
                ('emails_T', models.EmailField(max_length=254)),
                ('hw', models.TextField(max_length=1000)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.cl')),
            ],
        ),
    ]