from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
from rest_framework.views import APIView
##from .serializers import UserSerializers

# Create your views here.
class LoginView(APIView):

	def post(self, request, format=None):
		try:
			data = request.DATA
		except ParseError as error:
			return Response('Invalid JSON - {0}'.format(error.detail), status=status.HTTP_400_BAD_REQUEST)
		if "email" not in data or "password" not in data:
			return Response(
			'Wrong credentials', status=status.HTTP_401_UNAUTHORIZED)
		user = User.objects.first()
		if not user:
			return Response('No default user, please create one', status=status.HTTP_404_NOT_FOUND)
		token = Token.objects.get_or_create(user=user)
		return Response({'token': token[0].key})