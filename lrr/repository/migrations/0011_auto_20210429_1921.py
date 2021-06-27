# Generated by Django 3.1.4 on 2021-04-29 14:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('repository', '0010_competence_okso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drstatus',
            name='digital_resource',
        ),
        migrations.RemoveField(
            model_name='drstatus',
            name='edu_program',
        ),
        migrations.RemoveField(
            model_name='drstatus',
            name='expertise_status',
        ),
        migrations.RemoveField(
            model_name='drstatus',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='providingdiscipline',
            name='edu_program',
        ),
        migrations.RemoveField(
            model_name='providingdiscipline',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='subjecttheme',
            name='thematic_plan',
        ),
        migrations.RemoveField(
            model_name='thematicplan',
            name='edu_program',
        ),
        migrations.RemoveField(
            model_name='thematicplan',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='digitalresource',
            name='conformity_theme',
        ),
        migrations.RemoveField(
            model_name='digitalresource',
            name='provided_disciplines',
        ),
        migrations.DeleteModel(
            name='ConformityTheme',
        ),
        migrations.DeleteModel(
            name='DRStatus',
        ),
        migrations.DeleteModel(
            name='ExpertiseStatus',
        ),
        migrations.DeleteModel(
            name='ProvidingDiscipline',
        ),
        migrations.DeleteModel(
            name='SubjectTheme',
        ),
        migrations.DeleteModel(
            name='ThematicPlan',
        ),
    ]
