# Generated by Django 3.2.6 on 2021-08-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0035_alter_indicatorgroup_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusrequirement',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Используется'),
        ),
    ]
