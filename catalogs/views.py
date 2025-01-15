from django.shortcuts import render, redirect
from .models import Category


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            Category.objects.create(
                name = name,
                description = description
            )
            return redirect('home')
    return render(request, 'catalogs/category-create.html')