# Generated by Django 3.1.10 on 2021-05-14 02:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='per_discipline',
            field=models.BooleanField(default=False, verbose_name='Для каждой дисциплины'),
        ),
    ]
