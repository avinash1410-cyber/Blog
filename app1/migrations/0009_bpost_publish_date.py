# Generated by Django 2.2 on 2021-09-16 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_bpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpost',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]