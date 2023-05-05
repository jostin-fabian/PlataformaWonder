from django.shortcuts import render
from django.contrib.auth import  get_user_model
# Create your views here.

User = get_user_model()

def chatPage(request):
        users = User.objects.exclude(username=request.user.username)
        return render(request, 'wonder/entornoVirtual_HTML.html', context={'users':users})