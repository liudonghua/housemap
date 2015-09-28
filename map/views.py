from django.shortcuts import render

# Create your views here.

def index(request):
        contents    = Bdmap
        return render(request, 'map/index.html')