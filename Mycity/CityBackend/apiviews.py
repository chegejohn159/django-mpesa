from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword

class UserCreate(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer

class LoginView(APIView):

	permission_classes = ()
	serializer_class = UserSerializer
	def post(self, request,):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)
		if user:
			return Response({"token": user.auth_token.key})
		else:
			return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

