from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import ProductModel
from contact.models import ConatctModel
from home.models import Logo


logo = Logo.objects.all()
contact = ConatctModel.objects.all()
product = ProductModel.objects.all()


class OilsListView(View):
    def get(self, request):
        return render(request, 'oils/product.html', {'product':product , 'contact':contact, 'logo':logo})
    



class OilsDetailView(DetailView):
    model = ProductModel
    template_name = 'oils/productdetail.html'
    