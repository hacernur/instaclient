# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('hashtag', models.CharField(verbose_name='HashTag', max_length=100)),
                ('search_count', models.PositiveIntegerField(verbose_name='Search Count', default=0)),
                ('is_defective', models.BooleanField(verbose_name='Defective HashTag', default=False)),
            ],
            options={
                'verbose_name_plural': 'HashTags',
                'verbose_name': 'Hashtag',
            },
        ),
    ]
