# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_score', models.IntegerField(default=0)),
                ('guest_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='player',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='secondName',
            new_name='second_name',
        ),
        migrations.AddField(
            model_name='match',
            name='guest_team',
            field=models.ForeignKey(related_name='guest_team', to='bot.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='bot.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=None, to='bot.Team'),
            preserve_default=False,
        ),
    ]
