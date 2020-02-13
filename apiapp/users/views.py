from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.http import HttpRequest

from .models import User

# USER RELATED
class UserCreate(APIView):

	serializer_class = UserSerializer

	def post(self, request):
		try:
			data = request.data
		except ParseError as error:
			return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
		fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'password']
		for f in fields:
			if f not in data:
				return Response('Wrong credentials'+ str(data), status=status.HTTP_401_UNAUTHORIZED)
		serializer = self.serializer_class(data=data)
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response('Account could not be created', status=HTTP_400_BAD_REQUEST)		

class LoginView(APIView):

	def post(self, request, format=None):
		try:
			data = request.POST
		except ParseError as error:
			return Response('Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST)
		if "email" not in data or "password" not in data:
			return Response(
			'Wrong credentials'+str(request.data), status=status.HTTP_401_UNAUTHORIZED)
		user = User.objects.first()
		if not user:
			return Response('No default user, please create one', status=status.HTTP_404_NOT_FOUND)
		token = Token.objects.get_or_create(user=user)
		return Response({'token': token[0].key})

@api_view(['POST'])
def req(request):
		try:
			data = request.data
			if len(data) < 1:
				return Response('Empty', status=status.HTTP_404_NOT_FOUND)
		except ParseError as error:
			return Response('Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST)
		
		return Response('Wrong credentials '+str(data), status=status.HTTP_401_UNAUTHORIZED)
		