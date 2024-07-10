from django.urls import path
from shop import views as shop_views
from products.views import product_search

from payments.api import api_views as payment_view

urlpatterns = [
    path('', shop_views.ShopHome, name='home'),
    path('contact/', shop_views.ContactView, name='contact'),
    path('about/', shop_views.AboutUsView, name='about'),
    path('products/', shop_views.product_list, name='product_list'),
    path('products/search', product_search, name='search'),
    # Payments app API urls
    path('api/cart/add/', payment_view.add_to_cart_api, name='add_to_cart_api'),
    path('api/cart/details/', payment_view.cart_details_api, name='cart_details_api'),
]