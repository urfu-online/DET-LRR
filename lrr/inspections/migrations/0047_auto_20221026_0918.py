# Generated by Django 3.2.16 on 2022-10-26 04:18

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import lrr.inspections.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0025_alter_competence_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Название')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Порядок отображения')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ExpertiseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_published', models.BooleanField(default=True, verbose_name='Users can see it and answer it')),
                ('need_logged_user', models.BooleanField(verbose_name='Only authenticated users can see it and answer it')),
                ('editable_answers', models.BooleanField(default=True, verbose_name='Users can edit their answers afterwards')),
                ('display_method', models.SmallIntegerField(choices=[(1, 'By question'), (2, 'By category'), (0, 'All in one page')], default=0, verbose_name='Display method')),
                ('template', models.CharField(blank=True, max_length=255, null=True, verbose_name='Template')),
                ('publish_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Publication date')),
                ('expire_date', models.DateField(blank=True, default=lrr.inspections.models.in_duration_day, verbose_name='Expiration date')),
            ],
            options={
                'verbose_name': 'вид экспертизы',
                'verbose_name_plural': 'виды экспертизы',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OpinionIndicator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Последние обновление')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('discipline', auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.subject', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'показатель заключения',
                'verbose_name_plural': 'показатели заключения',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='indicator',
            options={'ordering': ('expertise_type', 'order'), 'verbose_name': 'показатель', 'verbose_name_plural': 'показатели'},
        ),
        migrations.RenameField(
            model_name='expertiseopinion',
            old_name='expertise',
            new_name='request',
        ),
        migrations.RemoveField(
            model_name='expertiseopinion',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='group',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='json_values',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='num_values',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='question',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='title',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='values',
        ),
        migrations.AddField(
            model_name='indicator',
            name='choices',
            field=models.TextField(blank=True, help_text='Поле выбора используется только в том случае, если тип вопроса\nесли тип вопроса - "радио", "выбор" или\n\'select multiple\' - список разделенных запятыми\nварианты этого вопроса .', null=True, verbose_name='Choices'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.subject', verbose_name='Дисциплина'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='inspections.indicator'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='text',
            field=models.TextField(null=True, verbose_name='Наименование показателя'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='type',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer'), ('float', 'float'), ('date', 'date')], default='text', max_length=200, verbose_name='Type'),
        ),
        migrations.DeleteModel(
            name='IndicatorGroup',
        ),
        migrations.AddField(
            model_name='opinionindicator',
            name='expertise_opinion',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinion_indicators', to='inspections.expertiseopinion', verbose_name='Экспертное заключение'),
        ),
        migrations.AddField(
            model_name='opinionindicator',
            name='indicator',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinion_indicators', to='inspections.indicator', verbose_name='Показатель'),
        ),
        migrations.AddField(
            model_name='category',
            name='expertise_type',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='inspections.expertisetype', verbose_name='Вид экспертизы'),
        ),
        migrations.AddField(
            model_name='expertiseopinion',
            name='expertise_type',
            field=auto_prefetch.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='inspections.expertisetype', verbose_name='Вид экспертизы'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='category',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='indicators', to='inspections.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='expertise_type',
            field=auto_prefetch.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='inspections.expertisetype', verbose_name='Вид экспертизы'),
        ),
    ]
