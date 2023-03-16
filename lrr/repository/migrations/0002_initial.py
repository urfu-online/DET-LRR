# Generated by Django 4.1.7 on 2023-03-15 18:42

import auto_prefetch
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("repository", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="digitalresource",
            name="authors",
            field=models.ManyToManyField(
                blank=True,
                related_name="authors_digital_resource",
                to="users.person",
                verbose_name="Авторы",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="competences",
            field=models.ManyToManyField(
                blank=True, to="repository.competence", verbose_name="Компетенции"
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="copyright_holder",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="repository.organization",
                verbose_name="Правообладатель",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="edu_programs_tags",
            field=models.ManyToManyField(
                blank=True,
                to="repository.eduprogramtag",
                verbose_name="Теги образовательных программ ЭОР",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="language",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="repository.language",
                verbose_name="Язык ресурса",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="owner",
            field=auto_prefetch.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="owner_digital_resource",
                to="users.person",
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="platform",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="repository.platform",
                verbose_name="Платформа",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="result_edu",
            field=models.ManyToManyField(
                blank=True,
                to="repository.resultedu",
                verbose_name="Образовательный результат",
            ),
        ),
        migrations.AddField(
            model_name="digitalresource",
            name="subjects_tags",
            field=models.ManyToManyField(
                blank=True,
                to="repository.subjecttag",
                verbose_name="Теги дисциплин ЭОР",
            ),
        ),
        migrations.AddField(
            model_name="bookmarkdigitalresource",
            name="obj",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="repository.digitalresource",
                verbose_name="Паспорт ЭОР",
            ),
        ),
        migrations.AddField(
            model_name="bookmarkdigitalresource",
            name="user",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="subjectchild",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="repository.subject",
                verbose_name="дисциплина",
            ),
        ),
        migrations.AddField(
            model_name="eduprogramchild",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="repository.eduprogram",
                verbose_name="образовательная программа",
            ),
        ),
    ]
