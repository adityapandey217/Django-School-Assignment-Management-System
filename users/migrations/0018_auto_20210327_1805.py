# Generated by Django 3.1 on 2021-03-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210327_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='section',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=100, null=True),
        ),
    ]