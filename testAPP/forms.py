#Attach my Product model to a ModelForm so I can save from form to my model.
#Next use this form in a view and displayit in a template.

#https://www.pydanny.com/core-concepts-django-modelforms.html
#https://tutorial.djangogirls.org/en/django_forms/
#https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/
#https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/

from django import forms
from .models import Product

class ProductForm(forms.ModelForms):
    class Meta:
        model = Product
        fields = '__all__'
