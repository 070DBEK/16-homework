from django.shortcuts import render, redirect
from .models import Color


def create_color(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hex_code = request.POST.get('hex_code')
        if name and hex_code:
            Color.objects.create(
                name = name,
                hex_code = hex_code
            )
            return redirect('home')
    return render(request, 'colors/color-create.html')