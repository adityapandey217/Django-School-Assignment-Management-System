# Generated by Django 3.1 on 2021-04-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_notification_general'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_general',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
