from .models import Category

def top_level_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    return {'top_level_categories': categories}