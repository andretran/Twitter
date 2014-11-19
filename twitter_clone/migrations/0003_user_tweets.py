# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_clone', '0002_user_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tweets',
            field=models.ForeignKey(related_name='author', default='Hello', to='twitter_clone.User'),
            preserve_default=False,
        ),
    ]
