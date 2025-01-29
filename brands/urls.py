from django.urls import path
from . import views


app_name = 'brands'


urlpatterns = [
    path('brand-create/', views.create_brand, name='create')
]