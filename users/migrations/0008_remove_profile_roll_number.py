# Generated by Django 3.1 on 2021-03-27 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210327_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roll_number',
        ),
    ]
