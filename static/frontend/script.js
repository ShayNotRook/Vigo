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
});

function checkout() {
    alert('Proceed to checkout')
}

