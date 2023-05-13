# Generated by Django 4.1.7 on 2023-05-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0005_alter_coldcoffeeshop_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coldcoffeeshop',
            old_name='paid',
            new_name='payment_failed',
        ),
        migrations.AddField(
            model_name='coldcoffeeshop',
            name='payment_success',
            field=models.BooleanField(default=False),
        ),
    ]
