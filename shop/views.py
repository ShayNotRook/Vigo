from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def ShopHome(request):
    welcome_test = "Welcome to Vigo!"
    user = get_user_model()
    return render(request, 'home.html', {'welcome_text': welcome_test, 'user': user})