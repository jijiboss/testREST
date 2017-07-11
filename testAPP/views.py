from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):


    #request.FILES is a dictionary that will contain the key for each FileField in the form.
    #The data here will be accessible as "request.FILES['file']"
    #This will only happen if the request method was POST, otherwise request.FILES will be empty.
    from .forms import ProductForm
    def import_csv(request):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                #prods = form.save(commit=False) #This tells not to commit this to DB just yet
                #---Do some stuff with the data before commiting to the DB
                #prods.save() #Now save to DB
                return render("uploaded.html", RequestContext(request))
        else:
            form = ProductForm()
        return render(request, "upload_end.html")


    def get(self, request, format=None):
        prods = Product.objects.all()
        serializer = ProductSerializer(prods, many=True) #tells there are multiple data
        return Response(serializer.data)

#    def post(self):
