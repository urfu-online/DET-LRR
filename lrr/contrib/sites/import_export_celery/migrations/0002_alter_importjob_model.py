# Generated by Django 3.2.9 on 2022-05-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_export_celery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importjob',
            name='model',
            field=models.CharField(max_length=160, verbose_name='Name of model to import to'),
        ),
    ]
