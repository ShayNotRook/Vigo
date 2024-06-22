from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_protect
# Create your views here.

# User = get_user_model()

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile_view.html', {'user': user})



class CustomLogoutView(View):
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
    
    def get(self, request, *args, **kwargs):
        return redirect('profile') # Redirect to a profile if accessed via GET