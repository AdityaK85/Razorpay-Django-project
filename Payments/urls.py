from django.urls import path
from .import views
urlpatterns = [
    
    path('home/', views.home),
    path('payment_status/', views.payment_status),
   
]
