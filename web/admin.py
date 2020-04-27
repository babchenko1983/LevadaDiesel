from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','number']
    list_display = ['name','number','slug','active','price','stock']
    list_editable = ['active', 'stock', 'price']
    prepopulated_fields = {'slug':('number',)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
