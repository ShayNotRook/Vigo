from django.views.generic import TemplateView
from django.views import View

from django.shortcuts import render

from django.contrib.auth import get_user_model

user = get_user_model()

class ContactView(TemplateView):
    template_name = 'contact-us.html'
    
def base_context(request):
    return render(request, 'base.html', {'user': user})
    