from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.
class CreateUser(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super(generics.CreateAPIView, self).create(request, *args,
                                                              **kwargs)
        return Response({
            'message': 'User created',
            'data': response.data
        }, status=status.HTTP_200_OK)

class UserLogin(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            
            login(request, user)
            user_details = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            }

           
          
            return Response(
                {"user_details": user_details,
                 "message": "Logged in sucessfully"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Authentication Failed"},
                status=status.HTTP_404_NOT_FOUND
            )
