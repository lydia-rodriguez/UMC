# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0008_auto_20151130_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='user_groups',
            field=models.IntegerField(default=4, choices=[(1, b'Administrators'), (2, b'Developers'), (3, b'DevelopersNew'), (4, b'Users')]),
            preserve_default=False,
        ),
    ]
