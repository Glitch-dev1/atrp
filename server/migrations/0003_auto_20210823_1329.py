# Generated by Django 3.1.5 on 2021-08-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20210823_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Url',
            field=models.URLField(null=True),
        ),
    ]