# Generated by Django 2.0.7 on 2018-07-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_auto_20180725_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='week',
            field=models.DateField(),
        ),
    ]
