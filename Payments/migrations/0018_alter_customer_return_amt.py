# Generated by Django 4.1.7 on 2023-05-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0017_delete_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='return_amt',
            field=models.FloatField(null=True, verbose_name='Return Amount'),
        ),
    ]
