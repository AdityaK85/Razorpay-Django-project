# Generated by Django 4.1.7 on 2023-05-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0009_coldcoffeeshop_mobile_coldcoffeeshop_upi_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coldcoffeeshop',
            name='amount',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
