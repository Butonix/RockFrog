# Generated by Django 2.2.5 on 2020-01-07 06:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0014_auto_20200107_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 14, 32, 188332), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 14, 32, 189333), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='communities.GroupArticle'),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 14, 32, 190334), verbose_name='date published'),
        ),
    ]
