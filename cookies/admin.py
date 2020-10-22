from django.contrib import admin

from .models import Cookie, Location, Order


class CookieAdmin(admin.ModelAdmin):
    def render_price(self, obj):
        return f'${obj.price}'
    render_price.short_description = 'Price'
    
    def render_rating(self, obj):
        return f'{obj.rating}/5'
    render_rating.short_description = 'Rating'

    list_display = ('name', 'render_price', 'render_rating', 'img_preview')
    list_display_links = ('name', 'render_price', 'render_rating')
    readonly_fields = ('img_preview',)
    list_filter = ('price',)
    search_fields = ('name', )


class LocationAdmin(admin.ModelAdmin):

    def render_avg_sale(self, obj):
        return f'${obj.avg_sale}'
    render_avg_sale.short_description = 'Average Sale'

    def render_min_customers(self, obj):
        return f'{obj.min_customers} customers/hour'
    render_min_customers.short_description = 'Minimum customers per hour'
    render_min_customers.short_description = 'Minimum customers per hour'

    def render_max_customers(self, obj):
        return f'{obj.max_customers} customers/hour'
    render_max_customers.short_description = 'Maximum customers per hour'

    list_display = ('name', 'manager', 'render_min_customers',
                    'render_max_customers', 'render_avg_sale')
    list_display_links = ('name', 'manager', 'render_min_customers',
                          'render_max_customers', 'render_avg_sale')

class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('date_placed', 'get_items')


admin.site.register(Cookie, CookieAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Order, OrderAdmin)
