from django.contrib import admin
from .models import Product


admin.site.register(Product)

admin.site.site_header = "My Django"
admin.site.site_title = 'Admin'
admin.site.index_title = 'Index title'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')