from django.shortcuts import render
from django.http import HttpResponse

# Hardcoded data for products
products = [
    {"name": "Laptop", "category": "Electronics", "price": "1000", "description": "High performance laptop.", "image": "https://via.placeholder.com/150"},
    {"name": "Smartphone", "category": "Electronics", "price": "600", "description": "Latest smartphone with all features.", "image": "https://via.placeholder.com/150"},
    {"name": "Headphones", "category": "Electronics", "price": "200", "description": "Noise-cancelling headphones.", "image": "https://via.placeholder.com/150"},
    {"name": "T-shirt", "category": "Clothing", "price": "20", "description": "Comfortable cotton t-shirt.", "image": "https://via.placeholder.com/150"},
    {"name": "Jeans", "category": "Clothing", "price": "40", "description": "Stylish denim jeans.", "image": "https://via.placeholder.com/150"},
]

# Hardcoded categories
categories = list(set([product["category"] for product in products]))

def homepage(request):
    return render(request, 'home.html')

def products_view(request):
    return render(request, 'products.html', {'products': products})

def product_details_view(request, product_id):
    try:
        product = products[product_id]
    except IndexError:
        return HttpResponse("Product not found.", status=404)
    return render(request, 'product_details.html', {'product': product})

def categories_view(request):
    category_data = {category: sum(1 for p in products if p["category"] == category) for category in categories}
    return render(request, 'categories.html', {'categories': category_data})

def contact_view(request):
    return render(request, 'contact.html')
