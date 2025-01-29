from django.urls import path
from . import views


app_name = 'colors'


urlpatterns = [
    path('color-create/', views.create_color, name='create')
]