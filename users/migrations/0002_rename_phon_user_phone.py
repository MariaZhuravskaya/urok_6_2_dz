# Generated by Django 4.2.4 on 2023-09-24 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phon',
            new_name='phone',
        ),
    ]
