from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Load
from .serializers import ProductSerializer

#Test HTML for tracking
def tracking(request):
    all_loads = Load.objects.all()
    myURL="https://maps.googleapis.com/maps/api/staticmap?center=39.8283,-98.5795&zoom=4&size=640x640&maptype=roadmap"

    #append each coordinate to the URL to map
    for load in all_loads:
        myURL += "&markers=size:mid|label:" + str(load.pk) +"|" + str(load.latitude) + "," + str(load.longitude)
    #Return the query result to display in the table and the URL to map
    return render(request, 'testAPP/APITest.html', {'all_loads': all_loads, 'myURL':myURL})


class ProductList(APIView):

    def get(self, request, format=None):
        prods = Product.objects.all()
        serializer = ProductSerializer(prods, many=True) #tells there are multiple data
        return Response(serializer.data)


#Update for django-import-export
from tablib import Dataset
from .resources import ProductResource

def import_csv(request):
    if request.method == 'POST':
        prod_resource = ProductResource()
        dataset = Dataset()

        new_prods = request.FILES['myfile'] #"myfile" comes form import.html form
        imported_data = dataset.load(new_prod.read())
        result = prod_resource.import_data(dataset, dry_run=True) #test the data import
        if not result.has_errors():
            prod_resource.import_data(dataset, dry_run=False) #commit for real
    return render(request, "upload_end.html")
