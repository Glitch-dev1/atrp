# Generated by Django 3.1.5 on 2021-08-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visamodel',
            name='textarea',
            field=models.TextField(),
        ),
    ]
