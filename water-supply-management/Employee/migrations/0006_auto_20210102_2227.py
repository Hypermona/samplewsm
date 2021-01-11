# Generated by Django 3.1.4 on 2021-01-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_auto_20210102_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AlterField(
            model_name='consumer',
            name='client_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
