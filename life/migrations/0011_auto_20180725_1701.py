# Generated by Django 2.0.7 on 2018-07-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0010_auto_20180725_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='week',
            field=models.DateField(),
        ),
    ]
