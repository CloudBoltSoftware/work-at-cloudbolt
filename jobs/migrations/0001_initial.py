# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title (e.g. position) for the job posting.', max_length=255, db_index=True)),
                ('description', models.TextField(help_text=b'Long-format description for this job posting.', max_length=2048)),
                ('posted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Location name', max_length=b'100', db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobposting',
            name='location',
            field=models.ForeignKey(to='jobs.Office'),
        ),
    ]
