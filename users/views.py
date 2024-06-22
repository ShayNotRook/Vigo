from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

@login_required
def profiel(request):
    user = request.user
    return render(request, 'users/profile_view.html', {'user': user})