from django.shortcuts import render
from django.views.generic import View
from .models import AboutusModel
from contact.models import ConatctModel
from home.models import Logo


logo = Logo.objects.all()
about = AboutusModel.objects.all()
contact = ConatctModel.objects.all()


class AboutusView(View):
    def get(self, request):
        return render(request, 'about_us/aboutus.html', {'about':about , 'contact':contact, 'logo':logo})