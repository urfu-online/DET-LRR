# Generated by Django 3.1.4 on 2021-03-11 07:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('inspections', '0003_auto_20210310_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckListBase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('protocol', models.CharField(max_length=424, verbose_name='№ Протокола учебно-методического совета института')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата проведения экспертизы')),
                ('status', models.CharField(blank=True, choices=[('START', 'Назначена'), ('IN_PROCESS', 'В процессе'), ('END', 'Завершена')], default='START', max_length=30, verbose_name='Состояние')),
                ('expert', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.expert', verbose_name='Эксперт')),
                ('expertise', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.expertise', verbose_name='Экспертиза')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_inspections.checklistbase_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.TextField(blank=True, help_text='Поле выбора используется только в том случае, если тип вопроса\nесли тип вопроса - "радио", "выбор" или\n\'select multiple\' - список разделенных запятыми\nварианты этого вопроса .', null=True, verbose_name='Выбор типа вопроса'),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer'), ('float', 'float'), ('date', 'date')], default='text', max_length=200, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.expert', verbose_name='Эксперт'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='protocol',
            field=models.CharField(blank=True, max_length=424, null=True, verbose_name='№ Протокола учебно-методического совета института'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='type',
            field=models.CharField(blank=True, choices=[('METHODIGAL', 'Методическая'), ('CONTENT', 'Содержательная'), ('TECH', 'Техническая'), ('NO_TYPE', 'Отсутствует тип экспертизы')], default='NO_TYPE', max_length=30, null=True, verbose_name='Тип чек-листа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Наименование показателя'),
        ),
        migrations.CreateModel(
            name='CheckListContent',
            fields=[
                ('checklistbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inspections.checklistbase')),
            ],
            options={
                'verbose_name': 'Чек-лист содержательной экспертизы',
                'verbose_name_plural': 'Чек-листы содержательных экспертиз',
            },
            bases=('inspections.checklistbase',),
        ),
        migrations.CreateModel(
            name='CheckListMethodical',
            fields=[
                ('checklistbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inspections.checklistbase')),
            ],
            options={
                'verbose_name': 'Чек-лист методической экспертизы',
                'verbose_name_plural': 'Чек-листы методических экспертиз',
            },
            bases=('inspections.checklistbase',),
        ),
        migrations.CreateModel(
            name='CheckListTechnical',
            fields=[
                ('checklistbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inspections.checklistbase')),
            ],
            options={
                'verbose_name': 'Чек-лист технической экспертизы',
                'verbose_name_plural': 'Чек-листы технических экспертиз',
            },
            bases=('inspections.checklistbase',),
        ),
        migrations.CreateModel(
            name='QuestionBase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.checklistbase', verbose_name='Чек-лист эеспертизы')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_inspections.questionbase_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Базовый опросник',
                'verbose_name_plural': 'Базовые опросники',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='checklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.checklistbase', verbose_name='Чек-лист эеспертизы'),
        ),
    ]
