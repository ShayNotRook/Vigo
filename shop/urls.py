from django.urls import path
from shop import views as shop_views
from products.views import product_search

urlpatterns = [
    path('', shop_views.ShopHome, name='home'),
    path('contact/', shop_views.ContactView, name='contact'),
    path('about/', shop_views.AboutUsView, name='about'),
    path('products/', shop_views.product_list, name='product_list'),
    path('products/search', product_search, name='search')
]