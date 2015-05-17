# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_auto_20150516_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='dish',
            field=models.ForeignKey(default=1, to='dishes.Dish'),
            preserve_default=False,
        ),
    ]
