# Generated by Django 3.1.5 on 2021-08-19 06:59

import Oauth.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='discorduser',
            managers=[
                ('objects', Oauth.managers.DiscordUserOauth2Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='discorduser',
            old_name='locate',
            new_name='locale',
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]
