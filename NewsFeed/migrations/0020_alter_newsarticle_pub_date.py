# Generated by Django 4.2.7 on 2023-11-11 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0019_alter_newsarticle_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 16, 46, 36, 527269, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
