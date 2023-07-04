from django.urls import path
from . import views



urlpatterns =[
    path('', views.CarsListView.as_view(), name="cars_list"),
    path('detail/<int:pk>', views.CarsDetailView.as_view(), name="cars_detail"),
]