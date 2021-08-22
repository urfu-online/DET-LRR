# Generated by Django 3.1.10 on 2021-05-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0025_auto_20210514_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorgroup',
            name='css_class',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='status',
            name='group',
            field=models.CharField(choices=[('qual', 'Категория качества контента ЭОР'), ('struct', 'Соответствие структуры и содержания ЭОР требованиям конкретных дисциплин ОП'), ('tech', 'Технологические возможности и сценарии функционирования ЭОР')], default='qual', max_length=6, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(db_index=True, max_length=1024, verbose_name='Наименование'),
        ),
    ]
