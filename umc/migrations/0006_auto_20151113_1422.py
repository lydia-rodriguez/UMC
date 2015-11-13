# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0005_auto_20151113_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_request',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique=True, serialize=False, primary_key=True),
        ),
    ]
