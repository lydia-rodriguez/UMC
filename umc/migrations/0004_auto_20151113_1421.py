# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0003_auto_20151113_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_request',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
