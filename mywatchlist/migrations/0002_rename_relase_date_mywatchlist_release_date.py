# Generated by Django 4.1.1 on 2022-10-06 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mywatchlist',
            old_name='relase_date',
            new_name='release_date',
        ),
    ]
