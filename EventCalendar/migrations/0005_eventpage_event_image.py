# Generated by Django 4.0.1 on 2022-03-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCalendar', '0004_rename_entry_final_date_eventpage_entry_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='event_image',
            field=models.CharField(default='null', max_length=300),
            preserve_default=False,
        ),
    ]
