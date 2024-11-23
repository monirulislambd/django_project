from django.shortcuts import render
from . models import Product

from django.views import View

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())

   
class ProductDetails(View):
    def get(self, request, pid):
        product = Product.objects.filter(id=pid)
        title = Product.objects.filter(id=pid).values('title')
        p_category = Product.objects.filter(category=product[0].category).exclude(id=pid).values('id', 'title')
        return render(request, 'app/product-details.html', locals())
    
