from django.shortcuts import render

def index(request):
    return render(request, 'app3/index.html')


# Create your views here.
