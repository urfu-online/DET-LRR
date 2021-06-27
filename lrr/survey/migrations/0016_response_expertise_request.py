# Generated by Django 3.1.4 on 2021-03-29 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inspections', '0007_expertiserequest_survey'),
        ('survey', '0015_auto_20210324_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='expertise_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='requests', to='inspections.expertiserequest',
                                    verbose_name='Заявка на экспертизу'),
        ),
    ]
