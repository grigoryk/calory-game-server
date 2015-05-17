# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_auto_20150516_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionalDataDish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('carbohydrates', models.IntegerField(null=True, blank=True)),
                ('protein', models.IntegerField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NutritionalDataGuess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('carbohydrates', models.IntegerField(null=True, blank=True)),
                ('protein', models.IntegerField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='dish',
            name='nutritional_data',
        ),
        migrations.RemoveField(
            model_name='guess',
            name='nutritional_data',
        ),
        migrations.DeleteModel(
            name='NutritionalData',
        ),
        migrations.AddField(
            model_name='nutritionaldataguess',
            name='guess',
            field=models.ForeignKey(related_name='nutritional_data', to='dishes.Guess'),
        ),
        migrations.AddField(
            model_name='nutritionaldatadish',
            name='dish',
            field=models.ForeignKey(related_name='nutritional_data', to='dishes.Dish'),
        ),
    ]
