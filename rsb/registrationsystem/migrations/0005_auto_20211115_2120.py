# Generated by Django 3.2.9 on 2021-11-15 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrationsystem', '0004_auto_20211115_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrollmentSummary',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registrationsystem.enrollmentsummary'),
        ),
        migrations.AlterField(
            model_name='course',
            name='gradeReport',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registrationsystem.gradereport'),
        ),
    ]