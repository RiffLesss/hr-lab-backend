# Generated by Django 5.0.4 on 2024-05-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cv_link',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
