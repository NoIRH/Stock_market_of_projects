# Generated by Django 4.0.1 on 2022-05-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSystem', '0002_role_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='CustomUser',
            name='user_bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='CustomUser',
            name='user_mask_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]