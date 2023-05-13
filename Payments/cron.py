from .models import *
import random

def print_hello():
    number = random.randint(0, 100)
    Category.objects.create(number = number)