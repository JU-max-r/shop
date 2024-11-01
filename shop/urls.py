from django.urls import path
from shop.views import *


urlpatterns = [
    path('catalog/', catalog),
    path('order/', order),
    path('product_detail/', product_detail),
    path('creative_order/', creative_order),
  
]










