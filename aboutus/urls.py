from django.urls import path
from . import views



urlpatterns = [
    path('', views.AboutusView.as_view(), name="aboutus"),
]