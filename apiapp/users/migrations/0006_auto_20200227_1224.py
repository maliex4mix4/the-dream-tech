# Generated by Django 3.0 on 2020-02-27 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200226_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 12, 24, 15, 359097)),
        ),
        migrations.AlterField(
            model_name='vendorsaccount',
            name='datecreated',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 27, 12, 24, 15, 374697)),
        ),
    ]