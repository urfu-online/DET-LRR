# Generated by Django 3.2.16 on 2022-10-26 02:20

import auto_prefetch
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0045_auto_20221026_0720'),
        ('users', '0030_auto_20211018_2339'),
        ('survey', '0024_auto_20221026_0720'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpertiseRequest',
        ),
        migrations.AddField(
            model_name='expertiseopinion',
            name='expert',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.expert', verbose_name='Эксперт'),
        ),
        migrations.AddField(
            model_name='expertiseopinion',
            name='expertise',
            field=auto_prefetch.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.request', verbose_name='Заявка'),
        ),
        migrations.AddField(
            model_name='expertiseopinion',
            name='survey',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='survey.survey', verbose_name='Вид экспертизы'),
        ),
    ]
