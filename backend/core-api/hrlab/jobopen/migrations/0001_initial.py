# Generated by Django 5.0.4 on 2024-05-23 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('requirements', models.CharField(max_length=2000)),
                ('salary', models.IntegerField()),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('is_archived', models.BooleanField(blank=True, default=False)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobs', to='project.project', verbose_name='Проект')),
            ],
            options={
                'db_table': 'job_open',
            },
        ),
    ]
