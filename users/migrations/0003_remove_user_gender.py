# Generated by Django 3.2.13 on 2023-08-25 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
