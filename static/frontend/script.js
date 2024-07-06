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

    // Hamburger Menu Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const menuContent = document.getElementById('menu-content');

    menuToggle.addEventListener('click', function() {
        menuContent.classList.toggle('active');
    });
});

function checkout() {
    alert('Proceed to checkout')
}