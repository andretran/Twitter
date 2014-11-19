# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_clone', '0003_user_tweets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tweets',
            field=models.ForeignKey(to='twitter_clone.Tweet'),
            preserve_default=True,
        ),
    ]
