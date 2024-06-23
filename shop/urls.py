from django.urls import path
from shop import views as shop_views
urlpatterns = [
    path('', shop_views.ShopHome, name='home')
]