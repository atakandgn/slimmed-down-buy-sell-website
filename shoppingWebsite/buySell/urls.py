# buySell/urls.py
from django.urls import path
from .views import home, product_detail, search_results

urlpatterns = [
    path('',  home, name='home'),
     path('product-detail/<int:ad_no>/', product_detail, name='product_detail'),
    path('search_results/', search_results, name='search_results'),
    
    
]