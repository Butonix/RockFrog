# Generated by Django 3.0.4 on 2020-03-24 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_messages', '0002_conversationlist_last_interaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationlist',
            name='last_interaction',
        ),
        migrations.AddField(
            model_name='conversation',
            name='last_interaction',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
