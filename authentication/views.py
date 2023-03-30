from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer,LoginSerializer
from rest_framework import response,status,permissions
from django.contrib.auth import authenticate

# Create your views here.

class AuthUserApiView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        user = request.user
        print(user)
        serializer = RegisterSerializer(user)
        return response.Response({'user':serializer.data})
class RegisterApiView(GenericAPIView):
    #to remove or bypass jwt validation
    authentication_classes =[]
    serializer_class = RegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginApiView(GenericAPIView):
    authentication_classes =[]
    #import login serializer
    serializer_class = LoginSerializer
    def post(self,request):
        incoming_data = request.data
        email = incoming_data.get("email",None)
        password = incoming_data.get("password",None)
        user = authenticate(username = email,password = password)
        if user:
            #log them in and send them a token
            serializer = self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            return response.Response({"message":"Invalid Credentials,try Again"},status=status.HTTP_401_UNAUTHORIZED)