# Generated by Django 4.1.5 on 2023-01-04 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_exl_files_exl_file2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exl_files',
            name='exl_file2',
        ),
    ]
