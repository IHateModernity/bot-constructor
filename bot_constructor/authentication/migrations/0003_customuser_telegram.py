# Generated by Django 4.1.1 on 2022-12-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telegram',
            field=models.CharField(blank=True, max_length=40, verbose_name='Телеграмм'),
        ),
    ]
