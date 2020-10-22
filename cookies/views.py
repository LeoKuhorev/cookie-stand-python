from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import LocationForm
from .models import Cookie, Location


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
        'items': cookies,
        'title': 'Welcome',
    }
    return render(request, 'cookies/home.html', context)


@login_required
def sales_data(request):
    user = request.user

    if user.is_staff:
        sales_data = Location.objects.all()

        context = {
            'user': user,
            'sales_data': sales_data,
            'title': 'Sales'
        }

        return render(request, 'cookies/sales.html', context)
    else:
        return HttpResponseForbidden("You don't have rights to access this page. Please contact your system administrator")


@login_required
def store_edit(request, store_id):
    store = Location.objects.get(pk=store_id)
    user = request.user
    if store.manager == user or user.is_superuser:
        if request.method == 'POST':
            form = LocationForm(request.POST, instance=store)
            for error in form.errors:
                messages.error(request, 'Form submission failed, please try again')

            if form.is_valid():
                form.save()
                messages.success(request, f'Store {store.name} has been updated')
                return redirect('sales')
        else:
            form = LocationForm(instance=store)

        context = {
            'form': form,
            'store': store,
            'title': f'Edit {store.name}',
        }
        return render(request, 'cookies/store_edit.html', context)

    else:
        return HttpResponseForbidden("You don't have rights to access this page. Please contact your system administrator")
