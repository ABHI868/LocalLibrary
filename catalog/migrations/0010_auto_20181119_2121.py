# Generated by Django 2.1.3 on 2018-11-19 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20181119_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedinuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logged_in_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
