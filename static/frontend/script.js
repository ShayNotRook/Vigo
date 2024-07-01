document.addEventListener('DOMContentLoaded', function() {
    const cart = document.getElementById('cart');
    const cartDetails = cart.querySelector('.cart-details');

    cart.addEventListener('click', function() {
        if (cartDetails.style.display === 'none' || cartDetails.style.display === '') {
            cartDetails.style.display = 'block';
        } else {
            cartDetails.style.display = 'none';
        }
    });
});

function checkout() {
    alert('Proceed to checkout')
}