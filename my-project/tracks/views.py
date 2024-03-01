from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
data = [
        {"id" : 1 , "name" : "python" },
        {'id' : 2 , "name" : 'java' }
        
    ]
@login_required()
def tracks(request):
    context = {"Data" : data}
    return render(request, 'tracks/tracks.html' , context)