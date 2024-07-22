document.addEventListener('DOMContentLoaded', function() {
    const menuContent = document.getElementById('menu-content');

    menuContent.addEventListener('click', function(event) {
        if (event.target.tagName === 'A' && event.target.dataset.slug) {
            event.preventDefault();
            const slug = event.target.dataset.slug;
            fetchCategoryData(slug);
            window.location.href = `/category/${slug}/`;
        }
    });

    function fetchCategoryData(slug) {
        const url = `api/categories/${slug}/products/`
        fetch(url)
            .then(response => response.json())
            .then(data => {
        updateCategoryView(data);
        })
        .catch(error => console.error('Error:', error));
        }

    function updateCategoryView(data) {
        const categoryContainer = document.getElementById('category-container');
        categoryContainer.innerHTML = '';

        if (data.subcategories && data.subcategories.length) {
        const subcategoryList = document.createElement('ul');
        subcategoryList.innerHTML = '<h2>Subcategories</h2>';
        data.subcategories.forEach(subcategory => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<a href="#" data-slug="${subcategory.slug}">${subcategory.title}</a>`;
            subcategoryList.appendChild(listItem)
        });
        categoryContainer.appendChild(subcategoryList);
        }

        if (data.products && data.products.length) {
        const productList = document.createElement('div');
        productList.className = 'product-list';
        productList.innerHTML = '<h2>Products</h2>';
        data.products.forEach(product => {
            const imageUrl = product.image_url ? product.image_url : '/static/default-cover.png';
            const productItem = document.createElement('div');
            productItem.className = 'product-item';
            productItem.innerHTML = `
                <img src='${imageUrl}' alt="${product.name}"> \
                <h3>${product.name}</h3> \
                <p>Price: $${product.price}</p>`;
            productList.appendChild(productItem);
            // console.log(product.image.url)
        });
        categoryContainer.appendChild(productList);
        }
    }
});