# Generated by Django 3.0 on 2020-02-27 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200227_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 13, 14, 34, 505912)),
        ),
        migrations.AlterField(
            model_name='vendorsaccount',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 13, 14, 34, 521512)),
        ),
    ]
