# Generated by Django 3.1 on 2021-03-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_profile_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='section',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
