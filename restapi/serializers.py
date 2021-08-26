from rest_framework import serializers
from .models import Product,Register
from django.contrib.auth.models import User




# class RegistrationSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=40)
#     email = serializers.EmailField(max_length=50)
#     password = serializers.CharField(max_length=50)
#     password2 = serializers.CharField(max_length=50)
#
#     class Meta:
#         model = User
#         fields = ('id',
#                   'username',
#                   'email',
#                   'password',
#                   'password2'
#                   )
#     def validation(self):
#         reg = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password']
#         if password != password2:
#             raise serializers.ValidationError({'password':'password does not match'})
#         reg.set_password(password)
#         reg.save()
#         return reg


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id',
                  'username',
                  'email',
                  'password',
                  )
        model = Register
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_added',
            'created',


        )
        model = Product