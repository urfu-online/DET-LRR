# Generated by Django 3.2.8 on 2021-10-18 14:43

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0022_alter_source_type'),
        ('users', '0029_remove_academicgroup_direction'),
        ('complexes', '0031_auto_20211018_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField(blank=True, null=True, verbose_name='Содержимое ячейки структурно-тематического плана')),
            ],
        ),
        migrations.RemoveField(
            model_name='cell',
            name='content',
        ),
        migrations.RemoveField(
            model_name='cell',
            name='end_point',
        ),
        migrations.RemoveField(
            model_name='cell',
            name='start_point',
        ),
        migrations.DeleteModel(
            name='Container',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='complex',
        ),
        migrations.AddField(
            model_name='theme',
            name='thematic_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='complexes.thematicplan'),
        ),
        migrations.AlterField(
            model_name='assignmentacademicgroup',
            name='academic_group',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.academicgroup', verbose_name='Академическая группа'),
        ),
        migrations.AlterField(
            model_name='digitalcomplex',
            name='language',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.language', verbose_name='Язык комплекса'),
        ),
        migrations.AlterField(
            model_name='digitalcomplex',
            name='owner',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner_digital_complex', to='users.person', verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='thematicplan',
            name='digital_complex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thematic_plan', to='complexes.digitalcomplex', verbose_name='Цифровой Комплекс (ЭУМК)'),
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
        migrations.AddField(
            model_name='component',
            name='thematic_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complexes.thematicplan'),
        ),
    ]
