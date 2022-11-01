# Generated by Django 3.2.16 on 2022-10-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acceptableindicatorvalue',
            options={'verbose_name': 'допустимое значение показателя', 'verbose_name_plural': 'допустимые значения показателя'},
        ),
        migrations.AlterModelOptions(
            name='summaryindicator',
            options={'verbose_name': 'сводный показатель', 'verbose_name_plural': 'сводные показатели'},
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='parent',
        ),
        migrations.AlterField(
            model_name='acceptableindicatorvalue',
            name='compliance',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Соответствие содержанию дисциплины (Полностью/Частично)'),
        ),
        migrations.AlterField(
            model_name='acceptableindicatorvalue',
            name='per_discipline',
            field=models.BooleanField(default=False, verbose_name='Для каждой дисциплины'),
        ),
        migrations.AlterField(
            model_name='summaryindicator',
            name='compliance',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Соответствие содержанию дисциплины (Полностью/Частично)'),
        ),
        migrations.AlterField(
            model_name='summaryindicator',
            name='per_discipline',
            field=models.BooleanField(default=False, verbose_name='Для каждой дисциплины'),
        ),
    ]
