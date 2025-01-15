from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from brands.models import Brand
from catalogs.models import Category
from colors.models import Color


def home(request):
    products = Product.objects.all()
    catalogs = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category__id=category_id)
    ctx = {'products':products, 'catalogs':catalogs}
    return render(request, 'index.html', ctx)


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        brand_id = request.POST.get('brand')
        category_id = request.POST.get('category')
        color_id = request.POST.get('color')
        image = request.FILES.get('image')
        if name and description and price and brand_id and category_id and color_id and image:
            brand = Brand.objects.get(id=brand_id)
            category = Category.objects.get(id=category_id)
            color = Color.objects.get(id=color_id)
            Product.objects.create(
                name = name,
                description = description,
                price = price,
                brand = brand,
                category = category,
                color = color,
                image = image
            )
            return redirect('home')
    brands = Brand.objects.all()
    catalogs = Category.objects.all()
    colors = Color.objects.all()
    ctx = {
        'brands':brands,
        'catalogs':catalogs,
        'colors':colors
    }
    return render(request, 'products/product-create.html', ctx)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    ctx = {'product':product}
    return render(request, 'products/product-detail.html', ctx)


def product_by_category(request):
    products = Product.objects.all()
    catalogs = Category.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    category_id = request.GET.get('category')
    brand_id = request.GET.get('brand')
    color_id = request.GET.get('color')
    if category_id:
                products = products.filter(category__id=category_id)
    if brand_id:
        products = products.filter(brand__id=brand_id)
    if color_id:
        products = products.filter(color__id=color_id)
    ctx = {
        'products':products,
        'catalogs':catalogs,
        'brands':brands,
        'colors':colors
    }
    return render(request, 'products/product-by-category.html', ctx)