# Generated by Django 2.2.5 on 2020-06-17 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0020_auto_20200615_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='not_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 10, 47, 12, 873416), verbose_name='date published'),
        ),
    ]
