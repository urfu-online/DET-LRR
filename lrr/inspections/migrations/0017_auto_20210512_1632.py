# Generated by Django 3.1.10 on 2021-05-12 11:32

import django_better_admin_arrayfield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inspections', '0016_auto_20210512_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='values',
            field=django_better_admin_arrayfield.models.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=32, null=True), blank=True, default=list, size=None),
        ),
    ]
