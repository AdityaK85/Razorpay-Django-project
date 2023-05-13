from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
import razorpay

@csrf_exempt
def home(request):
    if request.POST:
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100

        # Create Razorpay Client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SEC_KEY))

        # Create Razorpay Order
        response_payment = client.order.create( dict(amount = amount , currency = 'INR'))

        # order ID
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_id is not "" and order_status == "created":
            Customer.objects.create(
                name = name,
                amount = amount/100  ,
                order_id = order_id
            )

            response_payment['name'] = name

            context = {
                'KEY' : settings.RAZORPAY_KEY,
                'payment': response_payment
            }
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
 


@csrf_exempt
def payment_status(request):
    response = request.POST
    param_dict = {
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_signature' : response['razorpay_signature'],
    }

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SEC_KEY))
    try:
        status = client.utility.verify_payment_signature(param_dict)
        cust =  Customer.objects.get(order_id = response['razorpay_order_id'])
        cust.razor_payment_id = response['razorpay_payment_id']
        cust.payment_signature = response['razorpay_signature']
        cust.payment_success = True
        cust.status = True
        cust_amt = cust.amount
        

        web = website_ac.objects.get(id = 1)
        web.amount += cust_amt
        return_amt = cust_amt / 2
        cust.return_amt = return_amt
        web.amount -= return_amt

        web.save()
        cust.save()

        return render(request, 'payment_status.html', {'status': True})
    except:
        cust.razor_payment_id = response['Payments Failed by Customer']
        cust.payment_signature = response['Signature will be not Genrated " Payments Failed "']
        cust.payment_success = True
        cust.payment_failed = True

        return render(request, 'payment_status.html', {'status': False})
