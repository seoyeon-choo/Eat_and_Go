from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class BuyProductAdmin(admin.ModelAdmin):
    list_display=['category', 'name', 'slug', 'content', 'price', 'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable =['price', 'available_display', 'available_order']


admin.site.register(Buycategory, CategoryAdmin)
admin.site.register(Menu, BuyProductAdmin)