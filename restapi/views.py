from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import Product,Register, ProductSerializer ,RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

#
# class RegistrationSerializer(APIView):
#     serializer_class = RegistrationSerializer
#     def post(self,request):
#         data={}
#         serializer=RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             account=serializer.save()
#             data['response']='registered'
#             data['username']=account.username
#             data['email']=account.email
#             token,create=Token.objects.get_or_create(user=account)
#             data['token']=token.key
#         else:
#             data=serializer.errors
#         return Response(data)


class ListRegister(generics.ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class = RegistrationSerializer


class DetialRegister(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegistrationSerializer


class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


