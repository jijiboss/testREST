from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):

    def get(self, request, format=None):
        prods = Product.objects.all()
        serializer = ProductSerializer(prods, many=True) #tells there are multiple data
        return Response(serializer.data)

#    def post(self):
