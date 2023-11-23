# Generated by Django 4.2.5 on 2023-11-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='po_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='vendor_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]