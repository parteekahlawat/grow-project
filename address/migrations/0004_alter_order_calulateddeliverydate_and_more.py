# Generated by Django 4.1.6 on 2023-02-08 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_order_calulateddeliverydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='calulatedDeliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 8, 15, 9, 34, 591709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='estimatedDeliveryDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 8, 15, 9, 34, 591675, tzinfo=datetime.timezone.utc)),
        ),
    ]
