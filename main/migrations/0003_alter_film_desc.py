# Generated by Django 3.2.13 on 2023-10-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_film_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='desc',
            field=models.TextField(max_length=320),
        ),
    ]