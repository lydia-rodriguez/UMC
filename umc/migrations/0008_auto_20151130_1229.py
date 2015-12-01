# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umc', '0007_auto_20151113_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request',
            name='requestor_email',
            field=models.CharField(default='fname.lname@fsgi.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='requestor_first_name',
            field=models.CharField(default='fname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='requestor_last_name',
            field=models.CharField(default='lname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='user_email',
            field=models.EmailField(default='fname.lname@fsgi.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='user_first_name',
            field=models.CharField(default='fname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='user_last_name',
            field=models.CharField(default='lname', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_request',
            name='user_password',
            field=models.CharField(default='password1', max_length=50),
            preserve_default=False,
        ),
    ]
