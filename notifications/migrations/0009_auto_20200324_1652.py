# Generated by Django 3.0.4 on 2020-03-24 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20200102_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='not_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 16, 52, 25, 463998), verbose_name='date published'),
        ),
    ]
