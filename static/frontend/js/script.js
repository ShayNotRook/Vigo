document.addEventListener('DOMContentLoaded', function() {
    const cart = document.getElementById('cart');
    const cartDetails = cart.querySelector('.cart-details');

    cart.addEventListener('click', function(event) {
        if (!cartDetails.contains(event.target)) {
            if (cartDetails.style.display === 'none' || cartDetails.style.display === '') {
                cartDetails.style.display = 'block';
            } else {
                cartDetails.style.display = 'none';
            }
        }
    });

    cartDetails.addEventListener('click', function(event) {
        event.stopPropagation();
    })

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

    // Remove from Cart
    function attachRemoveListener() {
        document.querySelectorAll('.remove-from-cart').forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault()
                const itemId = this.dataset.itemId;
                const quantity = this.previousElementSibling.value;

                console.log('Item ID:', itemId); // Debuggin
                console.log('quantity:', quantity); // Debuggin

                if (!itemId || !quantity) {
                    console.error('Missing itemId or quantity');
                    return
                }

                removeFromCart(itemId, quantity);
                fetchCartDetails();
            })
        })
    }

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
                console.log(data)
                updateCartIcon(data.items.length, data.get_total_price);
                showCartNotification('Item added to cart!');
                fetchCartDetails();
            } else {
                alert('Failed to add item to cart.');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function removeFromCart(itemId, quantity) {
        fetch('/api/cart/remove/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                item_id: itemId,
                quantity: quantity
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); // Debugging: Log the data
            if (data.id) {
                updateCartIcon(data.items.length, data.get_total_price);
                showCartNotification('Item removed from cart!');
                fetchCartDetails();
            } else {
                alert('Failed to remove item from cart.');
            }
        })
        .catch(error => {
            console.error('Error', error);
            alert('An error occurred. Please try again.');
        });
    }

    function fetchCartDetails() {
        fetch(`/api/cart/details/`)
        .then(response => response.json())
        .then(data => {
            updateCartDetails(data.items, data.get_total_price);
            updateCartIcon(data.items.length, data.get_total_price);
        })
        .catch(error => console.error('Error:', error));
    }

    function updateCartIcon(itemCount, totalPrice) {
        const cartSummary = document.querySelector('.cart-summary .item-count');
        cartSummary.textContent = itemCount;
    }

    function updateCartDetails(items, totalPrice) {
        const cartDetails = document.querySelector('.cart-details ul');
        cartDetails.innerHTML = '';
        items.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `${item.content_object} (x${item.quantity}) - $${item.price} 
                <input type="number" min="1" max="${item.quantity}" value="1" class="remove-quantity" data-item-id="${item.id}">
                <button class="remove-from-cart" data-item-id="${item.id}">Remove</button>`;
            cartDetails.appendChild(li);
        });
        const total = document.createElement('p');
        total.textContent = `Total: $${totalPrice}`;
        cartDetails.appendChild(total);
        attachRemoveListener();
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
            notification.classList.add('fade');
            notification.addEventListener('transitionend', () => {
                notification.remove();
            });
        }, 5000);
    }

    // Fetch cart details when the page load
    fetchCartDetails();
    
    // Handle Checkout
    document.getElementById('checkout-button').addEventListener('click', function() {
        fetch('/api/cart/checkout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('Checkout successful! Order ID: ' + data.order_id);
                fetchCartDetails(); // Clear the cart after checkout
            } else {
                alert('Checkout failed. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during checkout. Please try again.');
        });
    });

});

function checkout() {
    alert('Proceed to checkout')
}

