# Generated by Django 3.2.6 on 2021-09-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_remove_academicgroup_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicgroup',
            name='direction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
