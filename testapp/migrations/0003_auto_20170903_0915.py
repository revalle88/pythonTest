# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20170903_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='retireDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
