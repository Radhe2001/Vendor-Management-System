# Generated by Django 4.2.5 on 2023-11-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0002_alter_purchaseordermodel_po_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancemodel',
            name='average_response_time',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='performancemodel',
            name='fulfillment_rate',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='performancemodel',
            name='on_time_delivery_rate',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='performancemodel',
            name='quality_rating_avg',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='average_response_time',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='fulfillment_rate',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='on_time_delivery_rate',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='quality_rating_avg',
            field=models.FloatField(default=100),
        ),
    ]
