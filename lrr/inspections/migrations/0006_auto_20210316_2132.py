# Generated by Django 3.1.4 on 2021-03-16 16:32

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210316_2132'),
        ('inspections', '0005_delete_questionbase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Значение показателя')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='CheckListQestion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('category', models.CharField(blank=True, choices=[('METHODIGAL', 'Методическая'), ('CONTENT', 'Содержательная'), ('TECH', 'Техническая'), ('NO_TYPE', 'Отсутствует тип экспертизы')], default='NO_TYPE', max_length=30, null=True, verbose_name='Категория чек-листа')),
            ],
            options={
                'verbose_name': 'Чек-лист',
                'verbose_name_plural': 'Чек листы',
            },
        ),
        migrations.CreateModel(
            name='ExpertiseRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('type', models.CharField(blank=True, choices=[('METHODIGAL', 'Методическая'), ('CONTENT', 'Содержательная'), ('TECH', 'Техническая'), ('NO_TYPE', 'Отсутствует тип экспертизы')], default='NO_TYPE', max_length=30, null=True, verbose_name='Тип заявки')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата проведения экспертизы')),
                ('protocol', models.CharField(blank=True, max_length=424, null=True, verbose_name='№ Протокола учебно-методического совета института')),
                ('status', models.CharField(blank=True, choices=[('START', 'Назначена'), ('IN_PROCESS', 'В процессе'), ('END', 'Завершена')], default='START', max_length=30, verbose_name='Состояние')),
                ('checklist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.checklistqestion', verbose_name='Чек-лист')),
                ('expert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.expert', verbose_name='Эксперт')),
                ('expertise', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.expertise', verbose_name='Экспертиза')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявка',
            },
        ),
        migrations.RemoveField(
            model_name='checklistbase',
            name='expert',
        ),
        migrations.RemoveField(
            model_name='checklistbase',
            name='expertise',
        ),
        migrations.RemoveField(
            model_name='checklistbase',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='checklistcontent',
            name='checklistbase_ptr',
        ),
        migrations.RemoveField(
            model_name='checklistmethodical',
            name='checklistbase_ptr',
        ),
        migrations.RemoveField(
            model_name='checklisttechnical',
            name='checklistbase_ptr',
        ),
        migrations.AddField(
            model_name='question',
            name='indicator_group',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Группа показателя'),
        ),
        migrations.DeleteModel(
            name='CheckList',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='checklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.checklistqestion', verbose_name='Чек-лист эеспертизы'),
        ),
        migrations.DeleteModel(
            name='CheckListBase',
        ),
        migrations.DeleteModel(
            name='CheckListContent',
        ),
        migrations.DeleteModel(
            name='CheckListMethodical',
        ),
        migrations.DeleteModel(
            name='CheckListTechnical',
        ),
    ]
