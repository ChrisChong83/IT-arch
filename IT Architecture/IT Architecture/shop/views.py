from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    return render(request, 'shop/index.html')

def products(request):
    products = Product.objects.all()  # Fetch products from the database
    return render(request, 'shop/products.html', {'products': products})

def cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render(request, 'shop/cart.html', {'cart': cart, 'total_price': total_price})

@login_required
def checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        return redirect('cart')  # Redirect to cart if empty
    total_price = sum(item['price'] for item in cart)
    if request.method == "POST":
        # Handle checkout logic (e.g., payment processing)
        # For simplicity, we just clear the cart after checkout
        request.session['cart'] = []
        return redirect('home')  # Redirect to home after checkout
    return render(request, 'shop/checkout.html', {'total_price': total_price})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/signin.html', {'form': form})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', [])
    cart.append({'name': product.name, 'price': float(product.price)})
    request.session['cart'] = cart
    return redirect('cart')
