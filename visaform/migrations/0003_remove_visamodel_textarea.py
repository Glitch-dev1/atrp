# Generated by Django 3.1.5 on 2021-08-17 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visaform', '0002_auto_20210817_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visamodel',
            name='textarea',
        ),
    ]
