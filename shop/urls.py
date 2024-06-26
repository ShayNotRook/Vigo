from django.urls import path
from shop import views as shop_views
urlpatterns = [
    path('', shop_views.ShopHome, name='home'),
    path('contact/', shop_views.ContactView, name='contact'),
    path('about/', shop_views.AboutUsView, name='about'),
]