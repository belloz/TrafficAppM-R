# Generated by Django 2.0.5 on 2018-05-09 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0003_auto_20180508_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tst',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 9, 13, 15, 58, 546004, tzinfo=utc)),
        ),
    ]
