# Generated by Django 3.0.4 on 2020-05-24 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_messages', '0004_auto_20200524_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='last_view_user1',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='conversation',
            name='last_view_user2',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
