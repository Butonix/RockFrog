# Generated by Django 2.2.5 on 2020-01-06 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0006_auto_20200106_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 14, 39, 2, 997823), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 14, 39, 2, 998824), verbose_name='date published'),
        ),
    ]