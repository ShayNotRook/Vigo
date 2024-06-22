from django.urls import path
from users import views as user_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('profile/', user_views.profile, name='profile_view'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_views.CustomLogoutView.as_view(), name='logout'),
]