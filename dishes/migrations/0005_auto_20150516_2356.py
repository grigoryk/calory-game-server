# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20150516_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionaldatadish',
            name='dish',
            field=models.OneToOneField(related_name='nutritional_data', to='dishes.Dish'),
        ),
        migrations.AlterField(
            model_name='nutritionaldataguess',
            name='guess',
            field=models.OneToOneField(related_name='nutritional_data', to='dishes.Guess'),
        ),
    ]
