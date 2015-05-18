# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20150517_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutritionaldatadish',
            name='cholesterol',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldatadish',
            name='fibre',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldatadish',
            name='sodium',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldatadish',
            name='sugar',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldataguess',
            name='cholesterol',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldataguess',
            name='fibre',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldataguess',
            name='sodium',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nutritionaldataguess',
            name='sugar',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='dish',
            field=models.ForeignKey(related_name='images', to='dishes.Dish'),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='calories',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='carbohydrates',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='fat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='protein',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='calories',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='carbohydrates',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='fat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='protein',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
