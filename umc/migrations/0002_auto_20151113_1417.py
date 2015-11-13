# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_request',
            name='id',
        ),
        migrations.AddField(
            model_name='user_request',
            name='request_num',
            field=models.AutoField(default=1111, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
