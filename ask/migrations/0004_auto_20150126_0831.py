# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_profile_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='ask.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='l_counter',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.AddField(
            model_name='answer',
            name='view_counter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='text_id',
            field=models.ForeignKey(default=1, to='ask.TextSet'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.ForeignKey(to='ask.TextSet'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.ForeignKey(to='ask.TextSet'),
            preserve_default=True,
        ),
    ]
