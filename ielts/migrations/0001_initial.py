# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('seatId', models.CharField(max_length=45, serialize=False, verbose_name='\u8003\u4f4d\u4ee3\u7801', primary_key=True)),
                ('center', models.CharField(max_length=45, verbose_name='\u8003\u70b9')),
                ('date', models.DateField(verbose_name='\u65e5\u671f')),
                ('city', models.CharField(max_length=45, verbose_name='\u57ce\u5e02')),
                ('province', models.CharField(max_length=45, verbose_name='\u7701\u4efd')),
                ('status', models.CharField(max_length=45, verbose_name='\u72b6\u6001')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'ordering': ['date', 'province', 'city', 'center'],
                'verbose_name': '\u8003\u4f4d\u4fe1\u606f',
                'verbose_name_plural': '\u8003\u4f4d\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
    ]
