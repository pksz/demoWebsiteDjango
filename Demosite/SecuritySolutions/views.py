from django.shortcuts import render
from .models import Products
# Create your views here.

def index(request):
    product=Products.objects.all().count(),
    product_description=Products.objects.all().count(),
    #product_image=Products.objects.get()

    context = { 'product':product,
    'product_description':product_description,
    #'product_image':product_image
    }

    return render(request,'index.html',context=context)