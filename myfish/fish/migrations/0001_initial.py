# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FishPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u4e8e')),
                ('photo', models.ImageField(upload_to=b'', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u9c7c\u7f38\u7167\u7247',
                'verbose_name_plural': '\u9c7c\u7f38\u7167\u7247',
            },
        ),
    ]
