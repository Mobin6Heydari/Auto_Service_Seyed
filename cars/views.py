from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import CarsModel
from contact.models import ConatctModel
from home.models import Logo


logo = Logo.objects.all()
cars = CarsModel.objects.all()
contact = ConatctModel.objects.all()


class CarsListView(View):
    def get(self, request):
        return render(request, 'cars/cars.html', {'cars':cars, 'contact':contact, 'logo':logo})
    



class CarsDetailView(DetailView):
    model = CarsModel
    template_name = 'cars/cars_detail.html'
    
    

