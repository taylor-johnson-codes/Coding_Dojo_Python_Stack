# Generated by Django 2.2.4 on 2020-07-24 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='replying_to',
        ),
    ]
