from django.shortcuts import render, redirect
from .models import Brand


def create_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        logo = request.FILES.get('logo')
        if name and description and logo:
            Brand.objects.create(
                name = name,
                description = description,
                logo = logo
            )
            return redirect('home')
    return render(request, 'brands/brand-create.html')