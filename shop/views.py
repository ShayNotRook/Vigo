from django.shortcuts import render


# Create your views here.
def ShopHome(request):
    welcome_test = "Welcome to Vigo!"
    return render(request, 'home.html', {'welcome_text': welcome_test})


def ContactView(request):
    return render(request, 'contact-us.html')