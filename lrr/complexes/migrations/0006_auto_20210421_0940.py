# Generated by Django 3.1.4 on 2021-04-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complexes', '0005_auto_20210326_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalcomplex',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование комплекса'),
        ),
    ]
