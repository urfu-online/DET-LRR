# Generated by Django 3.1.4 on 2021-04-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('repository', '0009_auto_20210427_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='okso',
            field=models.CharField(max_length=8, null=True, verbose_name='Код'),
        ),
    ]
