# Generated by Django 3.1.4 on 2021-04-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('complexes', '0007_auto_20210421_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='platformcomponent',
            options={'verbose_name': 'Среда обучения', 'verbose_name_plural': 'Среда обучения'},
        ),
        migrations.AlterModelOptions(
            name='traditionalsessioncomponent',
            options={'verbose_name': 'Синхронное занятие', 'verbose_name_plural': 'Синхронные занятия'},
        ),
        migrations.RemoveField(
            model_name='platformcomponent',
            name='platform',
        ),
        migrations.AddField(
            model_name='componentcomplex',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='description_self',
            field=models.TextField(blank=True, max_length=2024, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на онлайн-расписание занятий'),
        ),
        migrations.AlterField(
            model_name='componentcomplex',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True,
                                   verbose_name='Описание / Методика применения'),
        ),
        migrations.AlterField(
            model_name='literarysourcescomponent',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
