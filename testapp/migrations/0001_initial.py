# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sirname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('employDate', models.DateField(verbose_name=b'employment date')),
                ('retireDate', models.DateField()),
                ('occupation', models.CharField(max_length=100)),
                ('department', models.ForeignKey(to='testapp.Department')),
            ],
        ),
    ]
