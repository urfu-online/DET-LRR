# Generated by Django 3.2.9 on 2022-05-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0041_auto_20211018_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertise',
            name='status_text',
            field=models.TextField(blank=True, null=True, verbose_name='Статус'),
        ),
    ]
