from django.contrib import admin
from . models import Cart, Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_veg', 'is_available')
    list_display_links = ('name', 'category')
    list_editable = ('is_available', 'is_veg')


admin.site.register(Item, ItemAdmin)
admin.site.register(Cart)