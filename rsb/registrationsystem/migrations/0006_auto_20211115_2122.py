# Generated by Django 3.2.9 on 2021-11-15 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrationsystem', '0005_auto_20211115_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrollmentSummary',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registrationsystem.enrollmentsummary'),
        ),
        migrations.AlterField(
            model_name='course',
            name='gradeReport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='registrationsystem.gradereport'),
        ),
    ]