# Generated by Django 2.2.5 on 2020-01-07 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0013_auto_20200107_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 11, 1, 733309), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 11, 1, 734311), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 11, 1, 735311), verbose_name='date published'),
        ),
    ]
