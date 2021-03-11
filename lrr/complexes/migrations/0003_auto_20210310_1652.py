# Generated by Django 3.1.4 on 2021-03-10 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('complexes', '0002_auto_20210310_1652'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('repository', '0002_auto_20210310_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalcomplex',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner_digital_complex', to='users.person', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='digitalcomplex',
            name='results_edu',
            field=models.ManyToManyField(blank=True, to='repository.ResultEdu', verbose_name='Результаты обучения'),
        ),
        migrations.AddField(
            model_name='digitalcomplex',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='repository.Subject', verbose_name='Дисциплина(ы)'),
        ),
        migrations.AddField(
            model_name='componentcomplex',
            name='digital_complex',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='complexes.digitalcomplex', verbose_name='ЭУМК'),
        ),
        migrations.AddField(
            model_name='componentcomplex',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_complexes.componentcomplex_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='complextheme',
            name='digital_complex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complexes.digitalcomplex', verbose_name='Комплекс ЭМУК'),
        ),
        migrations.AddField(
            model_name='complexspacecell',
            name='cells',
            field=models.ManyToManyField(blank=True, to='complexes.Cell', verbose_name='Ячейка комплекса'),
        ),
        migrations.AddField(
            model_name='complexspacecell',
            name='digital_complex',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='complexes.digitalcomplex', verbose_name='Комплекс ЭМУК'),
        ),
        migrations.AddField(
            model_name='cellweeks',
            name='cell',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='complexes.cell', verbose_name='Ячейка комплекса'),
        ),
        migrations.AddField(
            model_name='assignmentacademicgroup',
            name='academic_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.academicgroup', verbose_name='Академическая группа'),
        ),
        migrations.AddField(
            model_name='assignmentacademicgroup',
            name='digital_complex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complexes.digitalcomplex', verbose_name='ЭУМКи'),
        ),
        migrations.AddField(
            model_name='assignmentacademicgroup',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='resourcecomponent',
            name='digital_resource',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='repository.digitalresource', verbose_name='ЭОР'),
        ),
        migrations.AddField(
            model_name='platformcomponent',
            name='platform',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='repository.platform', verbose_name='Платформа'),
        ),
    ]
