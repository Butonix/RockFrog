# Generated by Django 3.0.4 on 2020-03-24 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0009_auto_20200324_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='not_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 16, 56, 9, 654389), verbose_name='date published'),
        ),
    ]
