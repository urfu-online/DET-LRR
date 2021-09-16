# Generated by Django 3.1.10 on 2021-05-17 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0014_bookmarkdigitalresource'),
        ('users', '0007_groupdisciplines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupdisciplines',
            old_name='subject',
            new_name='subjects',
        ),
        # migrations.RemoveField(
        #     model_name='academicgroup',
        #     name='direction',
        # ),
        migrations.AddField(
            model_name='academicgroup',
            name='eduprogram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eduprogram_academic_group', to='repository.eduprogram', verbose_name='Образовательная программа/Направление подготовки'),
        ),
    ]
