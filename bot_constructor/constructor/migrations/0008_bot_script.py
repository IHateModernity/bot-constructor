# Generated by Django 4.0.6 on 2022-12-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0007_alter_command_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='script',
            field=models.FileField(blank=True, upload_to='files/', verbose_name='Script'),
        ),
    ]
