# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0006_auto_20151113_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1111, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_request',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
