# Generated by Django 2.1.1 on 2019-01-07 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='last_updates_time',
            new_name='last_updated_time',
        ),
    ]
