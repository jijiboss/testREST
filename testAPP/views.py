from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Load
from .serializers import ProductSerializer

#Test HTML for tracking
def tracking(request):
#    return render_to_response('testAPP/APITest.html')
    all_loads = Load.objects.all()
    return render(request, 'testAPP/APITest.html', {'all_loads': all_loads})

class ProductList(APIView):

    def get(self, request, format=None):
        prods = Product.objects.all()
        serializer = ProductSerializer(prods, many=True) #tells there are multiple data
        return Response(serializer.data)

#    def post(self):

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
