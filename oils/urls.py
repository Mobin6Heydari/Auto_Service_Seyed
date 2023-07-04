from django.urls import path
from . import views



urlpatterns =[
    path('', views.OilsListView.as_view(), name="product_list"),
    path('detail/<int:pk>', views.OilsDetailView.as_view(), name="product_detail"),
]