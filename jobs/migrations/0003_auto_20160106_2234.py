# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160106_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='description',
            field=models.TextField(help_text=b'Long-format description for this job posting.', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='location',
            field=models.ForeignKey(to='jobs.Office', blank=True),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='title',
            field=models.CharField(help_text=b'Title (e.g. position) for the job posting.', max_length=255, db_index=True, blank=True),
        ),
    ]
