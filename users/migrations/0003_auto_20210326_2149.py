# Generated by Django 3.1 on 2021-03-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210326_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]