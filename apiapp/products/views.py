from django.shortcuts import render

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .serializers import ProductsSerializers
from .models import Products

from .serializers import CategorySerializers
from .models import Category


class ProductsView(APIView):
    """docstring for ProductsView."""
    parser_class = (FileUploadParser)
    def get(self, request, format=None):
        product_ = Products.objects.all()
        serializer_ = ProductsSerializers(product_, many=True)
        return Response({"success": True, "payload": serializer_.data,})

    def post(self, request, *args, **kwargs):
        try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response({"success": False, "payload": error.detail,}, status=status.HTTP_400_BAD_REQUEST)

        product_serializer = ProductsSerializers(data=data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"success": True, "payload": {product_serializer.initial_data}, "info": "Product added"})

        else:
            return Response({"success": False, "payload": {}, "info": "Invalid Format."})


class ProductsList(APIView):
    parser_class = (FileUploadParser)
    def get_obj(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk):
        product_ = self.get_obj(pk)
        serializer_ = ProductsSerializers(product_)
        if serializer_:
            return Response({"success": True, "payload": serializer_.data, "info": "successful."})
        return Response({"success": False, "payload": {}, "info": "unknown error."})
    def put(self, request, pk):
        obj = self.get_obj(pk)
        serializer_ = ProductsSerializers(obj)
        if serializer_.is_valid():
            serializer_.save()
            return Response({"success": True, "payload": serializer_.data, "info": "Updated successfuly."})
    def delete(self, request, pk):
        obj = self.get_obj(pk)
        obj.delete()
        return Response({"success": True, "payload": {}, "info": "successful."})
