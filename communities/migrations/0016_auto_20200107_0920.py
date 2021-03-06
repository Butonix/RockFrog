# Generated by Django 2.2.5 on 2020-01-07 06:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0015_auto_20200107_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 20, 44, 728621), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='group',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grouparticle',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 20, 44, 730623), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usercomments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='groupcomment',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 7, 9, 20, 44, 731624), verbose_name='date published'),
        ),
    ]
