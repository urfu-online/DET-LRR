# Generated by Django 3.1.4 on 2021-03-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20210312_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='edu_level',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Уровень подготовки'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='standard',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Стандарт'),
        ),
    ]
