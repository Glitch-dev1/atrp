# Generated by Django 3.1.5 on 2021-09-01 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visaform', '0018_visamodel_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visamodel',
            old_name='date',
            new_name='date_created',
        ),
    ]