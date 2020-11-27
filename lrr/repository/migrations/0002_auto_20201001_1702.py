# Generated by Django 3.0.7 on 2020-10-01 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repository', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workplanacademicgroup',
            name='academic_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.AcademicGroup', verbose_name='Академическая группа'),
        ),
        migrations.AddField(
            model_name='workplanacademicgroup',
            name='digital_resource',
            field=models.ManyToManyField(to='repository.DigitalResource', verbose_name='Ресурсное обеспечение'),
        ),
        migrations.AddField(
            model_name='workplanacademicgroup',
            name='edu_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.EduProgram', verbose_name='Образовательная программа'),
        ),
        migrations.AddField(
            model_name='workplanacademicgroup',
            name='subject',
            field=models.ManyToManyField(to='repository.Subject', verbose_name='Дисциплины'),
        ),
        migrations.AddField(
            model_name='thematicplan',
            name='edu_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.EduProgram', verbose_name='Образовательная программа'),
        ),
        migrations.AddField(
            model_name='thematicplan',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.Subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='subjecttheme',
            name='thematic_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.ThematicPlan', verbose_name='Тематический план'),
        ),
        migrations.AddField(
            model_name='subjecttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='source',
            name='digital_resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.DigitalResource', verbose_name='Паспорт ЦОР'),
        ),
        migrations.AddField(
            model_name='resultedu',
            name='competence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.Competence', verbose_name='Компетенция'),
        ),
        migrations.AddField(
            model_name='providingdiscipline',
            name='edu_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.EduProgram', verbose_name='Образовательная программа'),
        ),
        migrations.AddField(
            model_name='providingdiscipline',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.Subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='eduprogramtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.EduProgram', verbose_name='Образовательная программа'),
        ),
        migrations.AddField(
            model_name='drstatus',
            name='digital_resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.DigitalResource', verbose_name='Паспорт ЦОР'),
        ),
        migrations.AddField(
            model_name='drstatus',
            name='edu_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.EduProgram', verbose_name='Утвержденная образовательная программа'),
        ),
        migrations.AddField(
            model_name='drstatus',
            name='expertise_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.ExpertiseStatus', verbose_name='Статус экспертизы'),
        ),
        migrations.AddField(
            model_name='drstatus',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.Subject', verbose_name='Утвержденная дисциплина'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='authors_digital_resource', to='users.Person', verbose_name='Авторы'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='conformity_theme',
            field=models.ManyToManyField(blank=True, to='repository.ConformityTheme', verbose_name='Соответствие ЦОР темам дисциплины'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='copyright_holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.Organization', verbose_name='Правообладатель'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='edu_programs_tags',
            field=models.ManyToManyField(blank=True, to='repository.EduProgramTag', verbose_name='Тэги образовательных программ ЦОР'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.Language', verbose_name='Язык ресурса'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner_digital_resource', to='users.Person', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.Platform', verbose_name='Платформа'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='provided_disciplines',
            field=models.ManyToManyField(blank=True, to='repository.ProvidingDiscipline', verbose_name='ЦОР рекомендован в качестве обеспечения дисциплины'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='result_edu',
            field=models.ManyToManyField(blank=True, to='repository.ResultEdu', verbose_name='Образовательный результат'),
        ),
        migrations.AddField(
            model_name='digitalresource',
            name='subjects_tags',
            field=models.ManyToManyField(blank=True, to='repository.SubjectTag', verbose_name='Тэги дисциплин ЦОР'),
        ),
        migrations.AddField(
            model_name='conformitytheme',
            name='providing_discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.ProvidingDiscipline', verbose_name='Рекомендация ЦОР в качестве обеспечения дисциплины'),
        ),
        migrations.AddField(
            model_name='conformitytheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.SubjectTheme', verbose_name='Тема дисциплины'),
        ),
    ]
