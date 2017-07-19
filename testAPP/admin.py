from django.contrib import admin
from .models import Product, Order
#admin.site.register(Product) #commented out in lieu of "@admin.register" to implement django-import-export
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource, OrderResource #import resource defintion for import-export


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('prod_id', 'name', 'description')
    resource_class = ProductResource #Used for import-export

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_id', 'name', 'qty')
    resource_class = OrderResource #Used for import-export
