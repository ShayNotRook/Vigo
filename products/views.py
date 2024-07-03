from django.shortcuts import render
from .forms import SearchForm
from .models import Game, GiftCard

def product_search(request):
    search_text = request.GET.get("search", "")
    products = set()
    form = SearchForm(request.GET)
    
    if form.is_valid():
        search = form.cleaned_data['search']
        products = (
            list(Game.objects.filter(name__icontains=search)) + 
            list(GiftCard.objects.filter(name__icontains=search))   
        )
        
    return render(request, 'search_results.html', {'form': form, 'products': products, 'search': search})
        
    