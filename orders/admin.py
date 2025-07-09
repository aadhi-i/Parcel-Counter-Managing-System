from django.contrib import admin
from .models import MenuItem, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status']
    inlines = [OrderItemInline]

admin.site.register(MenuItem)
admin.site.register(Order, OrderAdmin)
