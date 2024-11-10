from sqlite3 import IntegrityError
from django.shortcuts import render # type: ignore
from api.models import CustomUser
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .serializer import RegistrationSerializer, UserSerializer
from django.db.utils import IntegrityError # type: ignore
from rest_framework import generics # type: ignore

from rest_framework import status # type: ignore

from django.contrib.auth import authenticate # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore # Correct import

## ============================================= Create your views here. ================================================== ##

# get_user for taking user from
@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name': "Pedro", "age": 23}).data)

""" ---------------------------- Registration of User --------------------------- """
@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()  # Try to save the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            # Handle the IntegrityError for duplicate username
            if 'UNIQUE constraint failed' in str(e):
                return Response(
                    {"error": "A user with this username already exists."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {"error": "An error occurred during registration."},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get "Registrar User List"
@api_view(['GET'])
def get_registrar_users_list(request):
    customUserList = CustomUser.objects.all()
    serializer = RegistrationSerializer(customUserList, many=True)
    return Response(serializer.data)

# authentication with login
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        # Get or create the token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        # Prepare the response data with user profile and token
        user_data = {
            'username': user.username,
            'name': user.name,
            'phone_number': user.phone_number,
            'token': token.key,
        }
        
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

