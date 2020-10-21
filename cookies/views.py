from django.shortcuts import render
from .models import Cookie

def home(request):
    items = Cookie.objects.all().order_by('id')
    
    cookies = []
    for item in items:
        rating = []
        for i in range(1, 6):
            if i > item.rating:
                rating.append('grey')
            else:
                rating.append('blue')
        item.rating = rating
        cookies.append(item)
            
    
    context = {
        'items':cookies
    }
    return render(request, 'cookies/home.html', context)
