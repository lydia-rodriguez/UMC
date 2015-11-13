# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0004_auto_20151113_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_request',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_request',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, serialize=False, primary_key=True),
        ),
    ]
