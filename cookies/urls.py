from django.urls import path
from .views import home, sales_data, store_edit


urlpatterns = [
    path('', home, name='home'),
    path('sales/', sales_data, name='sales'),
    path('store/<int:store_id>/edit', store_edit, name='edit-store'),
]
