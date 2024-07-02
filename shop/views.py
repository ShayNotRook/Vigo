from django.shortcuts import render
from products.models import Game, GiftCard

# Create your views here.
def ShopHome(request):
    welcome_test = "Welcome to Vigo!"
    return render(request, 'home.html', {'welcome_text': welcome_test})


def ContactView(request):
    return render(request, 'contact-us.html')


def AboutUsView(request):
    from .utils import load_about_us
    
    about_us_content = load_about_us()
    context = {
        'about_us': about_us_content
    }
    
    return render(request, 'about.html', context)


def product_list(request):
    games = Game.objects.all()
    giftcards = GiftCard.objects.all()
    products = list(games) + list(giftcards)
    return render(request, 'products.html', {'products': products})