# Generated by Django 3.2.16 on 2022-11-02 13:13

import auto_prefetch
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0004_remove_acceptableindicatorvalue_per_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinionindicator',
            name='acceptable_indicator_value',
            field=auto_prefetch.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opinion_indicators', to='inspections.acceptableindicatorvalue', verbose_name='Значение показателя'),
        ),
    ]
