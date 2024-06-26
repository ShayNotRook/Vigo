from django.shortcuts import render


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