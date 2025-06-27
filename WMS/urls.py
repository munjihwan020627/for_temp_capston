from django.urls import path

from . import views

urlpatterns = [
path('add/product/', views.add_product, name='add_product'),
path('products/', views.product_list, name='product_list'),
path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
]