# Generated by Django 4.1.5 on 2023-01-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_exl_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='exl_files',
            name='exl_file2',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]