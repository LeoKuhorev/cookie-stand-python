from django.contrib import admin
from .models import Cookie, Location


class CookieAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class LocationAdmin(admin.ModelAdmin):

    def render_avg_sale(self, obj):
        return f'${obj.avg_sale}'

    def render_min_customers(self, obj):
        return f'{obj.min_customers} customers/hour'

    def render_max_customers(self, obj):
        return f'{obj.max_customers} customers/hour'

    list_display = ('name', 'manager', 'render_min_customers',
                    'render_max_customers', 'render_avg_sale')
    list_display_links = ('name', 'manager', 'render_min_customers',
                          'render_max_customers', 'render_avg_sale')


admin.site.register(Cookie, CookieAdmin)
admin.site.register(Location, LocationAdmin)
