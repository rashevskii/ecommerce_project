from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page, avialable=True)
    else:
        products = Product.objects.all().filter(avialable=True)
    return render(request, 'shop/home.html', {'catergory': category_page, 'products': products})


def product(request, category_slug, product_slug):
    try:
        products = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product': products})
