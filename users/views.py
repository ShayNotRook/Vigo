from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

# User = get_user_model()

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile_view.html', {'user': user})