# Generated by Django 3.1.12 on 2021-08-22 19:36

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0032_auto_20210823_0021'),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name='indicator',
            name='hstore_values',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='values',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=32, null=True), blank=True, null=True, size=None),
        ),
    ]
