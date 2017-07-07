import csv, sys, os
#Folder with manage.py
project_dir = "C:\\Users\msugimoto\Desktop\ProjectNoXL\DjangoPostgres\testREST\test_env\mySource\testAPI"

#Add the path to the system path
sys.path.append(project_dir)

#Designate which settings.py file to get the settings from  'mysite.settings'
#Note the settings.py is a "Python module with module-level variables"
#https://docs.djangoproject.com/en/1.11/topics/settings/
os.environ['DJANGO_SETTINGS_MODULE'] = 'testAPI.settings'

#Load the settings
import django
from django.conf import settings

#Start Django up for standalone, load my settings and populate Django's application registry
django.setup()


#Do whatever it is I need to do
from testAPP.models import Product

data = csv.reader(open(settings.MEDIA_ROOT + "\products.csv"), delimiter=",")

for row in data:
    if row[0] != 'product_id':
        prods = Product()
        prods.prod_id = row[0]
        prods.name = row[1]
        prods.description = row[2]
        prods.save()
