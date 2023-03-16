# Generated by Django 4.1.7 on 2023-03-15 18:42

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("repository", "0001_initial"),
        ("complexes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="digitalcomplex",
            name="competences",
            field=models.ManyToManyField(
                blank=True, to="repository.competence", verbose_name="Компетенции"
            ),
        ),
        migrations.AddField(
            model_name="digitalcomplex",
            name="directions",
            field=models.ManyToManyField(
                blank=True,
                to="repository.direction",
                verbose_name="Направления подготовки",
            ),
        ),
        migrations.AddField(
            model_name="digitalcomplex",
            name="keywords",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="complexes.UUIDTaggedItem",
                to="taggit.Tag",
                verbose_name="Ключевые слова",
            ),
        ),
        migrations.AddField(
            model_name="digitalcomplex",
            name="language",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="repository.language",
                verbose_name="Язык комплекса",
            ),
        ),
    ]
