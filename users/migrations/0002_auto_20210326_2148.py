# Generated by Django 3.1 on 2021-03-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='classes',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='roll',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
