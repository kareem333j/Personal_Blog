# Generated by Django 4.2.4 on 2023-08-19 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 17, 20, 52, 906713)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 17, 20, 52, 906713)),
        ),
    ]
