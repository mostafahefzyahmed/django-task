from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def hello(request):
        return render(request, 'home/home.html' , {'name':"Hello !"})