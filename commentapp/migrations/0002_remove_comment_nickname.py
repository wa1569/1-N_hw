# Generated by Django 3.0.5 on 2021-09-21 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='nickname',
        ),
    ]
