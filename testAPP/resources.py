#Create a “Resource” which defines how objects are mapped to their import/export representations and handle importing/exporting data.
#“ModelResource” on the other hand is a Resource subclass for handling Django models (scroll down towards the bottom for ModelResource)
#(http://django-import-export.readthedocs.io/en/latest/api_resources.html)
#Another description from Tastypie
#http://django-tastypie.readthedocs.io/en/latest/resources.html

from import_export import resources #import django_import_export package
from import_export import fields #To use with import_export in specifying the
from import_export.widgets import ForeignKeyWidget
from .models import Product, Order

#Define the characteristics and behaviors of the ModelResource of Product model object
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ['prod_id', 'name', 'description']

class OrderResource(resources.ModelResource):
    #Override the resource field, especially to define the ForeignKey widget and its details
    name = fields.Field(column_name='name', attribute='name', widget=ForeignKeyWidget(Product, 'name'))

    class Meta:
        model = Order
        skip_unchanged=True #Do not import existing unchaned objects
        #The default field for object identification is id, you can optionally set which fields are used as the id when importing:
        import_id_fields = ('name', )
        import_order = ('order_id', 'name', 'qty')
