# Generated by Django 4.0.1 on 2022-05-04 13:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DirectionsList',
            new_name='Direction',
        ),
        migrations.RenameModel(
            old_name='EntryStatuses',
            new_name='EntryStatus',
        ),
        migrations.RenameModel(
            old_name='EventTypes',
            new_name='EventType',
        ),
        migrations.RenameModel(
            old_name='ProjectEntries',
            new_name='ProjectEntry',
        ),
        migrations.RenameModel(
            old_name='ProjectResults',
            new_name='ProjectResult',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]