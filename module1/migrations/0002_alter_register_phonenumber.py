# Generated by Django 5.0 on 2024-01-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.PositiveBigIntegerField(),
        ),
    ]
