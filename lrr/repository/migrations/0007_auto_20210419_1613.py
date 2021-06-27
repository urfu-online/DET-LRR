# Generated by Django 3.1.4 on 2021-04-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('repository', '0006_auto_20210315_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Наименование')),
            ],
        ),
        migrations.AddField(
            model_name='direction',
            name='uni_id',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
    ]
