from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('register/', views.shop_register, name='shop_register'),
    path('shops/', views.shop_list, name='shop_list'),
    path('search/', views.shop_search, name='shop_search'),
]
