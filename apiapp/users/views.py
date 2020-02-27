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
from .models import EmailActivation
from .models import VendorsAccount

from .serializers import VendorSerializer

# USER RELATED
class VendorCreate(APIView):

	def post(self, request):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response({"success": False, "payload": error.detail,}, status=status.HTTP_400_BAD_REQUEST)

		user_create = VendorSerializer(data=data)
		if user_create.is_valid():
			user_create.save()
			return Response({
				"success": True,
				"payload": user_create.initial_data,
				"info": "Vendor Account activated."
			})
		else:
			return Response({"success": False, "payload": user_create.errors,})


class UserCreate(APIView):


	def post(self, request):
		try:
			data = request.data
			if len(data) < 1:
				data = request.query_params
		except ParseError as error:
			return Response({"success": False, "payload": error.detail,}, status=status.HTTP_400_BAD_REQUEST)

		user_create = UserSerializer(data=data)
		key_ = base64.b64encode(data['email'])
		if user_create.is_valid():
			user_create.save()
			new_activation = EmailActivation.objects.create(user=user, email=email, key=key_)
			new_activation.send_activation()
			return Response({
				"success": True,
				"payload": user_create.initial_data,
				"info": "User created. Please confirm Email."
			})
		else:
			return Response({"success": False, "payload": user_create.errors,})

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
				"success": False,
				"payload": {},
				"info": "No such user",
			})
		if obj.password != data['password']:
			return Response({
				"success": False,
				"payload": {},
				"info": "Invalid Username or password",
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

class EmailActivateView(APIView):

	def get(self, request, key=None):
		if key is not None:
			self.key = key
			qs = EmailActivation.objects.filter(key__iexact=key)
			confirm_qs = qs.confirmable()
			if confirm_qs.count() == 1:  # Not confirmed but confirmable
				obj = confirm_qs.first()
				obj.activate()
				return Response({"success": True, "payload": {}, "info": "Email Confirmed successfuly",})
			else:
				activated_qs = qs.filter(activated=True)
				if activated_qs.exists():
					return Response({"success": True, "info": "Email Confirmed Already",})
		return Response({"success": False, "payload": {}, "info": "Email coould not be activated.",})

		def post(self, request):
			try:
				data = request.data
				if len(data) < 1:
					data = request.query_params
			except ParseError as error:
				return Response({"success": False, "payload": error.detail,}, status=status.HTTP_400_BAD_REQUEST)

			user_exist = User.objects.filter(email=data['email']).first()
			key_ = base64.b64encode(data['email'])

			if user_exist:
				new_activation = EmailActivation.objects.create(user=user, email=email, key=key_)
				new_activation.send_activation()
			else:
				return Response({"success": False, "payload": user_create.errors,})
