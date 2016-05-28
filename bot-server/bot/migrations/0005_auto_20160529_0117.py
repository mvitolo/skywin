# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20160529_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Match', 'verbose_name_plural': 'Matches'},
        ),
    ]
