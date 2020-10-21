from django.shortcuts import render
from .models import Cookie, Location
from django.contrib.auth.decorators import login_required


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


@login_required
def sales_data(request):
    user = request.user
    print(user)
    sales_data = Location.objects.all()

    context = {
        'user': user,
        'sales_data': sales_data
    }

    return render(request, 'cookies/sales.html', context)