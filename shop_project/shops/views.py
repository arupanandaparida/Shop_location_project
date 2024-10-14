from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import Shop
from .utils import haversine

def home_view(request):
    return render(request, 'shops/home.html')


def shop_register(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list') 
    else:
        form = ShopForm()
    return render(request, 'shops/shop_register.html', {'form': form})


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shop_list.html', {'shops': shops})


def shop_search(request):
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')

    if user_lat is None or user_lon is None:
        
        return render(request, 'shops/shop_search.html', {'error': 'Please provide latitude and longitude.'})

    try:
        user_lat = float(user_lat)
        user_lon = float(user_lon)
    except (ValueError, TypeError):
        return render(request, 'shops/shop_search.html', {'error': 'Invalid latitude or longitude.'})

    shops = Shop.objects.all()
    shop_distances = [
        (shop, haversine(user_lat, user_lon, shop.latitude, shop.longitude))
        for shop in shops
    ]
    shop_distances.sort(key=lambda x: x[1])  # Sort by distance
    return render(request, 'shops/shop_search.html', {'shops': shop_distances})