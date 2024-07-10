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
    const overlay = document.getElementById('overlay');

    menuToggle.addEventListener('click', function() {
        menuContent.classList.toggle('active');
        overlay.classList.toggle('active');
    });

    // Close the menu when clicking the overlay
    overlay.addEventListener('click', function() {
        menuContent.classList.remove('active');
        overlay.classList.remove('active');
    });

    // Function to handle category click
    // function handleCategoryClick(event) {
    //     const categoryId = event.target.dataset.id; // Get the category ID\
    //     const url = '/category/${categoryId}/subcategories/'; // URL to fetch subcategories

    //     fetch(url)
    //         .then(response => response.json())
    //         .then(data => {
    //             const subcategoryList = document.getElementById('subcategory-list');
    //             subcategoryList.innerHTML = ''; // Clear any existing subcategories
    //             data.forEach(subcategory => {
    //                 var listItem = document.createElement('li');
    //                 listItem.textContent = subcategory.name;
    //                 subcategoryList.appendChild(listItem);
    //             });
    //         })
    //         .catch(error => {
    //             console.error('Error', error);
    //             alert('An error occured while loading subcategories');  
    //         });

    // }

    // // Attach event listeners to all top-level category items
    // var categoryItems = document.querySelectorAll('.top-level-category');
    // categoryItems.forEach(item => {
    //         item.addEventListener('click', handleCategoryClick);
    // });

    // Subcategory Toggle
    const topLevelCategories = document.querySelectorAll('.top-level-category');

    topLevelCategories.forEach(category => {
        category.addEventListener('click', function(event) {
            event.preventDefault();
            const subcategories = this.nextElementSibling;
            if (subcategories) {
                subcategories.classList.toggle('active');
                subcategories.style.display = subcategories.style.display === 'block' ? 'none': 'block';
            }
        });
    });

    // Add to Cart
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const contentTypeId = this.dataset.contentTypeId;
            const objectId = this.dataset.objectId;

            if (!contentTypeId || !objectId) {
                console.error('Missing contentTypeId or objectId');
                return;
            }
            addToCart(contentTypeId, objectId);
        });
    });

    function addToCart(contentTypeId, objectId) {
        fetch('/api/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                content_type_id: contentTypeId,
                object_id: objectId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.id) {
                updateCartIcon(data.items.length, data.get_total_price);
                showCartNotification('Item added to cart!');
            } else {
                alert('Failed to add item to cart.');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function fetchCartDetails() {
        fetch('/api/cart/details/')
        .then(response => response.json())
        .then(data => {
            updateCartDetails(data.items, data.get_total_price);
        })
        .catch(error => console.error('Error:', error));
    }

    function updateCartIcon(itemCount, totalPrice) {
        const cartSummary = document.querySelector('.cart-summary span');
        cartSummary.textContent = `${itemCount} Items - $${totalPrice}`;
    }

    function updateCartDetails(items, totalPrice) {
        const cartDetails = document.querySelector('.cart-details ul');
        cartDetails.innerHTML = '';
        items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.content_object} (x${item.quantity}) - $${item.price}`;
            cartDetails.appendChild(li);
        });
        const total = document.createElement('p');
        total.textContent = `Total: $${totalPrice}`;
        cartDetails.appendChild(total);
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function showCartNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'cart-notification';
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 2000);
    }
});

function checkout() {
    alert('Proceed to checkout')
}

