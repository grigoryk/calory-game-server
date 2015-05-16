# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20150516_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='photos',
            new_name='images',
        ),
    ]
