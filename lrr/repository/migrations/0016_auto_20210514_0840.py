# Generated by Django 3.1.10 on 2021-05-14 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0015_auto_20210514_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalresource',
            name='title',
            field=models.CharField(db_index=True, max_length=1024, verbose_name='Наименование ресурса'),
        ),
        migrations.AlterField(
            model_name='resultedu',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
    ]
