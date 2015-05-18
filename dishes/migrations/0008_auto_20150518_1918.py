# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0007_auto_20150518_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='calories',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='carbohydrates',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='cholesterol',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='fat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='fibre',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='protein',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='sodium',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='sugar',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='calories',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='carbohydrates',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='cholesterol',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='fat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='fibre',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='protein',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='sodium',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='sugar',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
