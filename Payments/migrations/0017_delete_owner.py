# Generated by Django 4.1.7 on 2023-05-12 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0016_alter_customer_amount_alter_customer_return_amt_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
