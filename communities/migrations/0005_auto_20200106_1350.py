# Generated by Django 2.2.5 on 2020-01-06 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20200106_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 13, 50, 18, 957312), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 13, 50, 18, 957312), verbose_name='date published'),
        ),
    ]
