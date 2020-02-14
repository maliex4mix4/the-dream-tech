from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer

from .models import User
from .forms import CustomUserCreationForm

# USER RELATED
class UserCreate(APIView):

	serializer_class = UserSerializer

	def post(self, request):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response('Error: '+error.detail, status=status.HTTP_400_BAD_REQUEST)
		fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'password']
		data_real = {}
		for f in fields:
			data_real[f] = data[f]
		serializer = self.serializer_class(data=data_real)
		serializer.create(validated_data)

		return Response(serializer.data, status=status.HTTP_201_CREATED)
	
class LoginView(ObtainAuthToken):
	serializer = UserSerializer
	def post(self, request, format=None):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response('Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST)
		serializer = self.serializer(data=data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
		    'token': token.key,
		    'user_id': user.pk,
		    'email': user.email,
		})
		#return Response('No default user, please create one', status=status.HTTP_404_NOT_FOUND)
		
