# Generated by Django 3.0.5 on 2020-04-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='input_file',
            field=models.FileField(blank=True, upload_to='input_files'),
        ),
        migrations.AlterField(
            model_name='file',
            name='output_file',
            field=models.FileField(blank=True, null=True, upload_to='output_files'),
        ),
    ]
