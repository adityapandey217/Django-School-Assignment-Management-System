# Generated by Django 3.1 on 2021-03-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210327_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='matric_number',
            new_name='roll_number',
        ),
    ]
