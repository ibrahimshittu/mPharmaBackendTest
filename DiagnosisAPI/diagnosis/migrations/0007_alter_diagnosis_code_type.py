# Generated by Django 4.0.1 on 2022-01-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0006_alter_diagnosis_code_alter_icd_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='code_type',
            field=models.CharField(choices=[('ICD_10', 'ICD_10'), ('ICD_9', 'ICD_9'), ('ICD_11', 'ICD_11')], default='ICD_10', max_length=1024),
        ),
    ]
