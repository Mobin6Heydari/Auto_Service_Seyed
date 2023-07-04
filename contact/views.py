from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ConatctModel, UserContactModel
from .forms import UserContactForm
from home.models import Logo


logo = Logo.objects.all()
contact = ConatctModel.objects.all()


class ContactView(View):
    def get(self, request):
        form = UserContactForm
        return render(request, 'contact/contact.html', {'contact' : contact, 'form': form, 'logo':logo})
    

    def post(self, request):
        form = UserContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            UserContactModel.objects.create(
                name = cd["name"],
                content = cd["content"],
                email = cd["email"],
                phone = cd['phone'],
                comment = cd['comment'],
            )
            return redirect('/')
        
        return render(request, 'contact/contact.html', {'form': form})