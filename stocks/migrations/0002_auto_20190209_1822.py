# Generated by Django 2.1.5 on 2019-02-09 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 9, 17, 22, 38, 680432, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.IntegerField(),
        ),
    ]
