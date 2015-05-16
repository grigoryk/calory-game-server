# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterModelOptions(
            name='guess',
            options={'verbose_name_plural': 'Guesses'},
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to=b'dish_images'),
            preserve_default=False,
        ),
    ]
