from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.products_view, name='products'),
    path('product/<int:product_id>/', views.product_details_view, name='product_details'),
    path('categories/', views.categories_view, name='categories'),
    path('contact/', views.contact_view, name='contact'),
]
