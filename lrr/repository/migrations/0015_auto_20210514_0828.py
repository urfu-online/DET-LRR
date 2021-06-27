# Generated by Django 3.1.10 on 2021-05-14 03:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('repository', '0014_bookmarkdigitalresource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencegroup',
            name='name',
            field=models.CharField(db_index=True, max_length=400, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='code',
            field=models.CharField(db_index=True, max_length=8, verbose_name='Код направления'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='title',
            field=models.CharField(db_index=True, max_length=450, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='language',
            name='title',
            field=models.CharField(db_index=True, max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Наименование'),
        ),
    ]
