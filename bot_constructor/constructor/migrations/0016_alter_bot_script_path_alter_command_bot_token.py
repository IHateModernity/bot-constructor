# Generated by Django 4.0.6 on 2022-12-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0015_alter_bot_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='script_path',
            field=models.CharField(default='', max_length=70, verbose_name='Path'),
        ),
        migrations.AlterField(
            model_name='command',
            name='bot_token',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Token'),
        ),
    ]
