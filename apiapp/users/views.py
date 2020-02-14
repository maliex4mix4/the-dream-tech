from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import authenticate

from .models import User


# USER RELATED
class UserCreate(APIView):


	def post(self, request):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response('Error: '+error.detail, status=status.HTTP_400_BAD_REQUEST)
		
		user_create = UserSerializer(data=data)
		if user_create.is_valid():
			user_create.save()
			return Response({
				"success": True,
				"payload": user_create.initial_data,
			})
		else:
			return Response({
				"error": user_create.errors,
			})
	
class LoginView(ObtainAuthToken):

	permission_classes = ()

	def post(self, request, format=None):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response('Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST)
		obj = User.objects.filter(email=data['email']).first()
		if not obj:
			return Response({
				"error": "No such user",
			})
		if obj.password != data['password']:
			return Response({
				"error": "Invalid Password",
			})
		token, created = Token.objects.get_or_create(user=obj)
		return Response({
			"success": True,
			"payload": {
				'token': token.key,
		    	'user_id': obj.pk,
		    	'email': obj.email,
			},
		})