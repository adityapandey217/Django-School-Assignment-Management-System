# Generated by Django 3.1 on 2021-03-31 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0021_notification_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('message', models.CharField(max_length=500)),
                ('files', models.ImageField(upload_to='notification/')),
                ('parents_avaviality', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
