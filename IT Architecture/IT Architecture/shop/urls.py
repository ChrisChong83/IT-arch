from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('index.html', views.home, name='home'),
    path('products.html/', views.products, name='products'),
    path('cart.html/', views.cart, name='cart'),
    path('checkout.html/', views.checkout, name='checkout'),
    path('signup.html/', views.signup, name='signup'),
    path('signin.html/', views.signin, name='signin'),
    path('', views.products, name='product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('products.html/index.html', views.home, name='home'),
    path('products.html/products.html/', views.products, name='products'),
    path('products.html/cart.html/', views.cart, name='cart'),
    path('products.html/checkout.html/', views.checkout, name='checkout'),
    path('products.html/signup.html/', views.signup, name='signup'),
    path('products.html/signin.html/', views.signin, name='signin'),



]
