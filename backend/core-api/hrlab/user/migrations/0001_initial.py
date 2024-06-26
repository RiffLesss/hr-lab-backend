# Generated by Django 5.0.4 on 2024-05-05 06:36

import django.utils.timezone
import hrlab.user.managers
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('login', models.CharField(max_length=25, unique=True)),
                ('first_name', models.CharField(max_length=600)),
                ('last_name', models.CharField(max_length=600)),
                ('middle_name', models.CharField(max_length=600)),
                ('education', models.CharField(max_length=600)),
                ('work_experience', models.CharField(blank=True, max_length=600, null=True)),
                ('project_experience', models.CharField(blank=True, max_length=600, null=True)),
                ('cv_link', models.CharField(max_length=600)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_staff', models.BooleanField(default=False, help_text='Indicates whether the user can log into this admin site.')),
                ('role', models.CharField(choices=[('Administrator', 'Admin'), ('Lab_Employee', 'Lab'), ('User', 'User')], default='User', max_length=20)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'ordering': ['id'],
            },
            managers=[
                ('objects', hrlab.user.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MethodPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='*', max_length=120)),
                ('users', models.ManyToManyField(related_name='user_method_permissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'method_permission',
            },
        ),
        migrations.CreateModel(
            name='ViewPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='*', max_length=120)),
                ('users', models.ManyToManyField(related_name='user_view_permissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'view_permission',
            },
        ),
    ]
