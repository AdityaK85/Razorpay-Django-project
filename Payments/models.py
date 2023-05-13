from django.db import models

# Create your models here.

class website_ac(models.Model):
    name = models.CharField( max_length=500)
    amount = models.FloatField(verbose_name="Bank Balance Amount",)


class Customer(models.Model):
    name  = models.CharField(max_length=1000)
    amount  = models.FloatField(verbose_name="Paid Amount",)
    mobile  = models.CharField(max_length=1000, null=True)
    return_amt  = models.FloatField(verbose_name="Return Amount",  null=True)
    upi_id  = models.CharField(max_length=1000, null=True)
    order_id  = models.CharField(max_length=1000 , blank=True)
    razor_payment_id  = models.CharField(max_length=1000 , blank=True)
    payment_signature  = models.CharField(max_length=1000 , blank=True)
    status = models.BooleanField(default=False)
    payment_success = models.BooleanField(default=False)
    payment_failed = models.BooleanField(default=False)