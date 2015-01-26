# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20150126_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='view_counter',
        ),
        migrations.AddField(
            model_name='question',
            name='view_counter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
