# Generated by Django 3.1 on 2021-04-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_notification_general_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification_general',
            name='files',
            field=models.ImageField(blank=True, null=True, upload_to='notification/'),
        ),
    ]
