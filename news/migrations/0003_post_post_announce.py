# Generated by Django 2.2.2 on 2019-06-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190630_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_announce',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
