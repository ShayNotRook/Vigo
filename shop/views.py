from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from products.models import Game, GiftCard, Category
from payments.models import Cart, CartItem

from .forms import ContactForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def ShopHome(request):
    welcome_test = "Welcome to Vigo!"
    return render(request, 'home.html', {'welcome_text': welcome_test})


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Message from {name} via Contact Form',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
            
    return render(request, 'contact.html', {'form': form})


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

@login_required
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        
    except Cart.DoesNotExist:
        cart = None
        
        
    context = {
        'cart': cart
    }
    
    return render(request, 'cart.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.get_all_products()
    subcategories = category.get_subcategories()
    
    context = {
        'category': category,
        'products': products,
        'subcategories': subcategories
    }
    
    return render(request, 'shop/category_detail.html', context)