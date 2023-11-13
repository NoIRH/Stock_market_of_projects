# Generated by Django 4.0.1 on 2022-05-18 10:06

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_alter_project_options_projectentry_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='project_participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_authors',
            field=models.ManyToManyField(related_name='project_authors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 10, 6, 26, 228044, tzinfo=utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 10, 6, 26, 230044, tzinfo=utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 10, 6, 26, 230044, tzinfo=utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
    ]
