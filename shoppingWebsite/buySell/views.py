from django.shortcuts import render
import requests

async def home(request):
    # Make a request to the endpoint for categories
    response = requests.get("https://run.mocky.io/v3/d87c545e-a41f-4cac-bb01-c5b11ebcd82b")
    
    if response.status_code == 200:
        categories = response.json().get('categories', [])
    else:
        categories = []
        
    # Make a request to the endpoint for products
    response = requests.get("https://run.mocky.io/v3/8eb44032-64e0-4f6f-ad31-fa0afc67977d")

    if response.status_code == 200:
        products = response.json().get('products', [])
    else:
        products = []

    # Split the products into chunks of 3 for the grid layout
    chunked_products = [products[i:i+3] for i in range(0, len(products), 3)]

    return render(request, 'home.html', {'categories': categories , 'chunked_products': chunked_products})

async def product_detail(request):
    return render(request, 'product_detail.html')

async def search_results(request):
    return render(request, 'search_results.html')

