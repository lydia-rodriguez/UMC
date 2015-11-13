# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0002_auto_20151113_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_request',
            old_name='request_num',
            new_name='id',
        ),
    ]
