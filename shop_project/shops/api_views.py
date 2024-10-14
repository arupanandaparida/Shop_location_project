# shops/api_views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shop
from .serializers import ShopSerializer
from .utils import haversine

class ShopListCreateAPIView(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopSearchAPIView(APIView):
    def get(self, request):
        user_lat = float(request.query_params.get('latitude'))
        user_lon = float(request.query_params.get('longitude'))
        shops = Shop.objects.all()
        shop_distances = [
            {'shop': ShopSerializer(shop).data, 'distance': haversine(user_lat, user_lon, shop.latitude, shop.longitude)}
            for shop in shops
        ]
        shop_distances.sort(key=lambda x: x['distance'])
        return Response(shop_distances, status=status.HTTP_200_OK)
