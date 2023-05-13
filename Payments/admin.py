from django.contrib import admin
from .models import *

class Web_Pattern(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')

class customer_Pattern(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'mobile', 'return_amt', 'upi_id', 'order_id', 'razor_payment_id', 'payment_signature', 'status', 'payment_success', 'payment_failed')

admin.site.register(website_ac, Web_Pattern)
admin.site.register(Customer , customer_Pattern)
