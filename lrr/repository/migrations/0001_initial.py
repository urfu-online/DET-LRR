# Generated by Django 3.1.4 on 2021-03-10 11:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Компетенция',
                'verbose_name_plural': 'Компетенции',
            },
        ),

        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('code', models.CharField(max_length=8, verbose_name='Код направления')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
            },
        ),
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=450, verbose_name='Наименование')),
                ('short_description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Короткое описание')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Образовательная программа',
                'verbose_name_plural': 'Образовательные программы',
            },
        ),
        migrations.CreateModel(
            name='DigitalResource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=1024, verbose_name='Наименование ресурса')),
                ('type', models.CharField(choices=[('OK', 'Онлайн-курс'), ('EUK', 'ЭУК'), ('TEXT_EOR', 'Текстовый электронный образовательный ресурс'), ('MULTIMEDIA_EOR', 'Мультимедийный электронный образовательный ресурс')], max_length=30, null=True, verbose_name='Тип ресурса')),
                ('source_data', models.CharField(choices=[('MANUAL', 'вручную'), ('IMPORT', 'импорт')], default='MANUAL', max_length=30, verbose_name='Источник данных')),
                ('keywords', models.CharField(blank=True, max_length=6024, null=True, verbose_name='Ключевые слова')),
                ('description', models.TextField(blank=True, max_length=6024, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Паспорт ЭОР',
                'verbose_name_plural': 'Паспорта ЭОР',
                'ordering': ['title'],
            },
        ),

        migrations.CreateModel(
            name='ExpertiseStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('end_date', models.DateTimeField(verbose_name='Срок действия')),
                ('status', models.CharField(choices=[('NO_INIT', 'не инициирована'), ('SUB_APP', 'подана заявка'), ('ON_EXPERTISE', 'на экспертизе'), ('ON_REVISION', 'на доработку'), ('ASSIGNED_STATUS', 'присвоен статус')], default='NO_INIT', max_length=30, verbose_name='Состояние экспертизы')),
                ('accepted_status', models.BooleanField(default=False, verbose_name='Утверждено (присвоен статус)')),
            ],
            options={
                'verbose_name': 'Статус экспертизы',
                'verbose_name_plural': 'Статусы экспертиз',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('title', models.CharField(max_length=80, verbose_name='Наименование')),
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Код языка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
            ],
            options={
                'verbose_name': 'Язык ресура',
                'verbose_name_plural': 'Языки ресурсов',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('url_logo', models.URLField(blank=True, null=True, verbose_name='Ссылка на логотип')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='upload/images/', verbose_name='Логотип')),
                ('contacts', models.TextField(blank=True, max_length=500, null=True, verbose_name='Контакты')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('url_logo', models.URLField(blank=True, null=True, verbose_name='Ссылка на логотип')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='upload/images/', verbose_name='Логотип')),
                ('contacts', models.TextField(blank=True, max_length=500, null=True, verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Платформа',
                'verbose_name_plural': 'Платформы',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('labor', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Трудоемкость')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='ThematicPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('edu_program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.eduprogram', verbose_name='Образовательная программа')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.subject', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Тематический план',
                'verbose_name_plural': 'Тематические планы',
            },
        ),
        migrations.CreateModel(
            name='SubjectTheme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наимаенование')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('thematic_plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.thematicplan', verbose_name='Тематический план')),
            ],
            options={
                'verbose_name': 'Тема дисциплины',
                'verbose_name_plural': 'Темы дисциплин',
            },
        ),
        migrations.CreateModel(
            name='SubjectTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.subject', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Тэг дисциплины',
                'verbose_name_plural': 'Тэги дисциплин',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('link_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование')),
                ('URL', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('file', models.FileField(blank=True, null=True, upload_to='upload/files', verbose_name='Файл')),
                ('type', models.CharField(blank=True, max_length=150, null=True, verbose_name='Тип')),
                ('digital_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.digitalresource', verbose_name='Паспорт ЭОР')),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='ResultEdu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('competence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.competence', verbose_name='Компетенция')),
            ],
            options={
                'verbose_name': 'Образовательный результат',
                'verbose_name_plural': 'Образовательные результаты',
            },
        ),
        migrations.CreateModel(
            name='ProvidingDiscipline',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('rate', models.PositiveIntegerField(verbose_name='Процент покрытия')),
                ('edu_program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.eduprogram', verbose_name='Образовательная программа')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='repository.subject', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Рекомендация ЭОР в качестве обеспечения дисциплины',
                'verbose_name_plural': 'Рекомендации ЭОР в качестве обеспечения дисциплин',
            },
        ),
        migrations.CreateModel(
            name='EduProgramTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.eduprogram', verbose_name='Образовательная программа')),
            ],
            options={
                'verbose_name': 'Тэг образовательной программы',
                'verbose_name_plural': 'Тэги образовательных программ',
            },
        ),
        migrations.CreateModel(
            name='DRStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('quality_category', models.CharField(blank=True, choices=[('INNER', 'внутренний'), ('OUTER', 'внешний'), ('OUTSIDE', 'сторонний')], max_length=30, verbose_name='Категория качества')),
                ('interactive_category', models.CharField(blank=True, choices=[('NOT_INTERACTIVE', 'не интерактивный'), ('WITH_TEACHER_SUPPORT', 'с поддержкой преподавателя'), ('AUTO', 'автоматизированный')], max_length=30, verbose_name='Категория интерактивности')),
                ('digital_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.digitalresource', verbose_name='Паспорт ЭОР')),
                ('edu_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.eduprogram', verbose_name='Утвержденная образовательная программа')),
                ('expertise_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.expertisestatus', verbose_name='Статус экспертизы')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='repository.subject', verbose_name='Утвержденная дисциплина')),
            ],
            options={
                'verbose_name': 'Статус ЭОР',
                'verbose_name_plural': 'Статусы ЭОР',
            },
        ),
        migrations.CreateModel(
            name='ConformityTheme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('practice', models.BooleanField(null=True, verbose_name='Практика')),
                ('theory', models.BooleanField(null=True, verbose_name='Теория')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
            ],
            options={
                'verbose_name': 'Соответствие ЭОР темам дисциплины',
                'verbose_name_plural': 'Соответствия ЭОР темам дисциплин',
            },
        ),
    ]
