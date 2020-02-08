from django.shortcuts import render

from rest_framework.decorators import app_view, permission_classses
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


@app_view(['GET'])
def restricted(request, *args, **kwargs):
	return Response(data='only for logged in user', status=status.HTTP_200_OK)