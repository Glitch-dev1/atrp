# Generated by Django 3.1.5 on 2021-08-21 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visaform', '0007_auto_20210821_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visamodel',
            name='user',
        ),
        migrations.AddField(
            model_name='visamodel',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='auth.user'),
            preserve_default=False,
        ),
    ]
