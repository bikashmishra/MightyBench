# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startusupapp', '0002_auto_20150418_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dribblelink',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
