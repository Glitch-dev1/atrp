# Generated by Django 3.1.5 on 2021-08-21 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visaform', '0008_auto_20210821_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visamodel',
            name='sender',
        ),
        migrations.AddField(
            model_name='visamodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
            preserve_default=False,
        ),
    ]
