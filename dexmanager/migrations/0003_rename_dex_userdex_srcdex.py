# Generated by Django 4.2.3 on 2023-07-12 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dexmanager', '0002_srcdex_userdex_delete_dex_srcdex_watching_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdex',
            old_name='dex',
            new_name='srcDex',
        ),
    ]