from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import Product


def index(request):
    return render(request, 'index.html')

# def team(request):
#     return render(request, 'index.html')
#
def contact(request):
    return render(request, 'contact.html')




class ItemDetailView(View):
    def get(self, request, slug):
        print("ok")
        product = Product.objects.get(slug=slug)
        return render(request, 'product.html', {"product": product})


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'shop.html', context)


class Search(ListView):
    template_name = 'shop1.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(number__icontains=query))
        return object_list
