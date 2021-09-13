# Generated by Django 3.1.5 on 2021-09-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facmodel',
            name='faction',
            field=models.CharField(choices=[('PD', '👮 Police Department 👮'), ('EMS', '🏥 Medical Department 🏥'), ('FBI', '🕵️ Federal Bureau Of Investigation 🕵️'), (' Mech', '🛠️ Mechanic 🛠️'), ('News', '📰Department of News📰')], max_length=160),
        ),
    ]