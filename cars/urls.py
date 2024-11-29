from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/car/<int:car_id>', views.car_detail_view, name='car_detail'),
]
