# Generated by Django 4.2.7 on 2023-11-12 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_project_pub_date_alter_projectentry_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 14, 36, 50, 569601, tzinfo=datetime.timezone.utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 14, 36, 50, 571601, tzinfo=datetime.timezone.utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 14, 36, 50, 571601, tzinfo=datetime.timezone.utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
        migrations.AlterField(
            model_name='projectnotice',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 12, 14, 36, 50, 573602, tzinfo=datetime.timezone.utc)),
        ),
    ]
