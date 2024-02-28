# Generated by Django 5.0 on 2024-01-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=3)),
                ('EmpName', models.CharField(max_length=200)),
                ('EmpGender', models.CharField(max_length=10)),
                ('EmpEmail', models.EmailField(max_length=254)),
                ('EmpDesignation', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Employee1',
            },
        ),
    ]
