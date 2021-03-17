# Generated by Django 3.1.4 on 2021-03-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complexes', '0003_auto_20210310_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentacademicgroup',
            name='semestr',
            field=models.CharField(blank=True, choices=[('FIRST', 'Первый семестр'), ('SECOND', 'Второй семестр')], max_length=12, null=True, verbose_name='Семестр'),
        ),
    ]
