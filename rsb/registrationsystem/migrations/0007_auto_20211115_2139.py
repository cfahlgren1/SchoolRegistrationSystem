# Generated by Django 3.2.9 on 2021-11-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationsystem', '0006_auto_20211115_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='professor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]