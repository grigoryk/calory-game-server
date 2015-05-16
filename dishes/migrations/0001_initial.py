# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('is_vegetarian', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dish', models.ForeignKey(to='dishes.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('carbohydrates', models.IntegerField(null=True, blank=True)),
                ('protein', models.IntegerField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='guess',
            name='nutritional_data',
            field=models.ForeignKey(to='dishes.NutritionalData'),
        ),
        migrations.AddField(
            model_name='guess',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dish',
            name='nutritional_data',
            field=models.ForeignKey(blank=True, to='dishes.NutritionalData', null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='photos',
            field=models.ManyToManyField(to='dishes.Image'),
        ),
    ]
