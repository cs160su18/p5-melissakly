# Generated by Django 2.0.7 on 2018-07-25 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0009_auto_20180725_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='week',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
