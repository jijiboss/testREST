from django.contrib import admin
from .models import Product, Order, Load
#admin.site.register(Product) #commented out in lieu of "@admin.register" to implement django-import-export
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource, OrderResource, LoadResource #import resource defintion for import-export


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('prod_id', 'name', 'description')
    resource_class = ProductResource #Used for import-export

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('order_id', 'name', 'qty')
    resource_class = OrderResource #Used for import-export

#For the model that stores coordinates so I can map them
@admin.register(Load)
class LoadAdmin(ImportExportModelAdmin):
    list_display = ('time_stamp', 'load_number', 'container_num', 'latitude', 'longitude')
    list_editable = ('load_number', 'container_num', 'latitude', 'longitude') #Editable table!
    resource_class = LoadResource #Used for import-export
