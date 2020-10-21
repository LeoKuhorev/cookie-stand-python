from django.urls import path
from .views import home, sales_data


urlpatterns = [
    path('', home, name='home'),
    path('sales/', sales_data, name='sales')
]
