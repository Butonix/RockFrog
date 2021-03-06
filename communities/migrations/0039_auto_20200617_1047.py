# Generated by Django 2.2.5 on 2020-06-17 07:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0038_auto_20200615_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouparticle',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 10, 47, 12, 867411), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 10, 47, 12, 870413), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 10, 47, 12, 872415), verbose_name='date published'),
        ),
    ]
