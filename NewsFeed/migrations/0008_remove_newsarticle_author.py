# Generated by Django 4.0.1 on 2022-05-07 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeed', '0007_alter_newsarticle_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='author',
        ),
    ]
