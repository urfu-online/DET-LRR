# Generated by Django 3.2.8 on 2021-10-18 17:06

import datetime
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import taggit.managers
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [('complexes', '0034_auto_20211018_2037'), ('complexes', '0035_auto_20211018_2200'), ('complexes', '0036_auto_20211018_2204')]

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('complexes', '0033_auto_20211018_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complexes_uuidtaggeditem_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complexes_uuidtaggeditem_items', to='taggit.tag')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.AlterField(
            model_name='digitalcomplex',
            name='keywords',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='complexes.UUIDTaggedItem', to='taggit.Tag', verbose_name='Ключевые слова'),
        ),
        migrations.AlterModelManagers(
            name='thematicplan',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='thematicplan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thematicplan',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последние обновление'),
        ),
        migrations.AlterField(
            model_name='thematicplan',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
