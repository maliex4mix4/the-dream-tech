from django.shortcuts import render

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductsSerializers

class ProductsView(APIView):
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        product_serializer = ProductsSerializers(data=data)

        if product_serializer.is_valid():
            product_serializer.save()

        else:
            return Response({"success": False, "payload": {}, "info": "Invalid Format."})
