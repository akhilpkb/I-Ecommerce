from . import views
from django.contrib import admin
from django.urls import include, path
app_name = 'ecomapp'

urlpatterns = [
    path('', views.allProductCat, name='allProductCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]   
