# Generated by Django 2.2 on 2021-09-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_bpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bpost',
            name='slug',
            field=models.SlugField(default='Slug'),
        ),
    ]
