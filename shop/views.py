from django.shortcuts import render

# Create your views here.
def home(request):
    welcome_test = "Welcome to Vigo!"
    return render(request, 'home.html', {'welcome_text': welcome_test})