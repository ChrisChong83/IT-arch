// Define the cart as an array
let cart = [];

// Function to add products to the cart
function addToCart(productName, price) {
    cart.push({ productName, price });
    localStorage.setItem('cart', JSON.stringify(cart)); // Store cart in localStorage
    alert(`${productName} added to cart!`);
}

// Function to load cart items dynamically
function loadCart() {
    cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartItems = document.getElementById('cart-items');
    const totalPrice = document.getElementById('total-price');
    let total = 0;

    cartItems.innerHTML = ''; // Clear current items
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.productName} - $${item.price}`;
        cartItems.appendChild(li);
        total += item.price;
    });

    totalPrice.textContent = total;
}

// Load cart items on cart page load
if (document.body.contains(document.getElementById('cart-items'))) {
    loadCart();
}
