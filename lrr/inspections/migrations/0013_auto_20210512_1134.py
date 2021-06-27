# Generated by Django 3.1.10 on 2021-05-12 06:34

import django.contrib.postgres.fields.ranges
import django_better_admin_arrayfield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inspections', '0012_auto_20210512_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='num_values',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='values',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=32),
                                                                          blank=True, default='', size=None),
        ),
    ]
