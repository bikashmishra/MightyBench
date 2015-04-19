# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startusupapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dribblelink',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='githublink',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedinlink',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
