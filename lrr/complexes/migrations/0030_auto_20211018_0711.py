# Generated by Django 3.2.8 on 2021-10-18 02:11

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('complexes', '0029_thematicplan'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='digitalcomplex',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='theme',
            name='content',
        ),
    ]
