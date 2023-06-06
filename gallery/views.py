from django.shortcuts import render

# Create your views here.

def homePage(request):

    return render(request, 'gallery/index.html')
