# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0009_user_request_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_request',
            name='user_groups',
            field=models.CharField(max_length=20, choices=[(b'Administrators', b'Administrators'), (b'Developers', b'Developers'), (b'DevelopersNew', b'DevelopersNew'), (b'Users', b'Users')]),
        ),
    ]
