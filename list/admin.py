from django.contrib import admin
from .models import Menu

# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'available_display', 'available_order')
#     list_filter = ('category', 'available_display', 'available_order')
#     prepopulated_fields = {'slug': ('name',)}
#     search_fields = ('name', 'category')
#     list_editable = ('available_display', 'available_order')

class BuyProductAdmin(admin.ModelAdmin):
    list_display=['name', 'slug', 'content', 'price', 'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable =['price', 'available_display', 'available_order']



admin.site.register(Menu, BuyProductAdmin)