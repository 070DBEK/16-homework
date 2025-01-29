from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from brands.models import Brand
from catalogs.models import Category
from colors.models import Color


def home(request):
    products = Product.objects.all()
    ctx = {'products':products}
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
    comments = Comment.objects.filter(product=product)
    if request.method == "POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        desc = request.POST.get('desc')
        if name and rating and desc:
            Comment.objects.create(
                product=product,
                name=name,
                rating=rating,
                desc=desc,
            )
        return redirect('products:detail', product_id=product.id)

    ctx = {
        'product': product,
        'comments': comments,
    }
    return render(request, 'products/product-detail.html', ctx)


def product_by_category(request):
    products = Product.objects.all()
    catalogs = Category.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()

    sort = request.GET.get('sort')

    category_id = request.GET.get('category')
    brand_name = request.GET.get('brand')
    color_name = request.GET.get('color')
    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')

    if sort == 'price-asc':
        products = products.order_by('price')
    elif sort == 'price-desc':
        products = products.order_by('-price')
    elif sort == 'name-asc':
        products = products.order_by('name')
    elif sort == 'name-desc':
        products = products.order_by('-name')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if category_id:
        products = products.filter(category__id=category_id)
    if brand_name:
        products = products.filter(brand__name=brand_name)
    if color_name:
        products = products.filter(color__name=color_name)
    ctx = {
        'products': products,
        'catalogs': catalogs,
        'brands': brands,
        'colors': colors,
        'sort': sort,
    }

    return render(request, 'products/product-by-category.html', ctx)




