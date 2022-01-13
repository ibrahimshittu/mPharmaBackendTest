# Generated by Django 4.0.1 on 2022-01-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='code_type',
            field=models.CharField(choices=[('ICD_10', 'ICD_10'), ('ICD_8a', 'ICD_8a'), ('ICD_9', 'ICD_9'), ('ICD-9-CM', 'ICD-9-CM'), ('ICD_11', 'ICD_11')], default=('ICD_10', 'ICD_10'), max_length=1024),
        ),
    ]
