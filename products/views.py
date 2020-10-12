from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    queryset    = Product.objects.all()

#function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html", context)