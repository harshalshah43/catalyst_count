# Generated by Django 4.2.13 on 2024-06-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='current_employee_estimate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='total_employee_estimate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
