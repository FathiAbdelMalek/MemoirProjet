# Generated by Django 3.2 on 2021-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='article_name',
            field=models.CharField(max_length=100),
        ),
    ]
