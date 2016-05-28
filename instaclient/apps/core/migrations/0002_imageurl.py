# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(verbose_name='Updated Time', auto_now=True)),
                ('url', models.CharField(verbose_name='URL', max_length=500)),
                ('hashtag', models.ForeignKey(verbose_name='HashTag', to='core.HashTag')),
            ],
            options={
                'verbose_name': 'Image Url',
                'verbose_name_plural': 'Image Urls',
            },
        ),
    ]
