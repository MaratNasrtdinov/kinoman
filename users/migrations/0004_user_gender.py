# Generated by Django 3.2.13 on 2023-08-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=None, max_length=8),
        ),
    ]
