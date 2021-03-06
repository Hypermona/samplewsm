# Generated by Django 3.1.4 on 2021-01-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20210102_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='username',
            field=models.CharField(default='hacker', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='hacker', max_length=30),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
