# Generated by Django 3.1.12 on 2021-08-06 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Тело статуса')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата выставления статуса')),
                ('expertise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.expertise', verbose_name='Экспертиза')),
            ],
            options={
                'verbose_name': 'Временный статус',
                'verbose_name_plural': 'Временные статусы',
            },
        ),
    ]
