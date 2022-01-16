# Generated by Django 4.0.1 on 2022-01-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0005_icd_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='code',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='icd_file',
            name='file',
            field=models.FileField(upload_to='icd_codes/'),
        ),
    ]
