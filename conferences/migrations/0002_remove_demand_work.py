# Generated by Django 3.1.7 on 2021-04-04 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand',
            name='work',
        ),
    ]
