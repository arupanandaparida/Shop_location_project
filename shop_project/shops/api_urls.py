from django.urls import path
from .api_views import ShopListCreateAPIView, ShopSearchAPIView

urlpatterns = [
    path('shops/', ShopListCreateAPIView.as_view(), name='shop-list-create'),
    path('shops/search/', ShopSearchAPIView.as_view(), name='shop-search'),
]
