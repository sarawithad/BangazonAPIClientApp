from django.contrib.auth.models import User, Group
from rest_framework import serializers
from API.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Author: Steve Brownlee
    """
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class RestrictedCustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Author: Steve Brownlee
    """
    class Meta:
        model = Customer
        fields = (
            'id', 
            'url', 
            'first_name', 
            'last_name', 
        )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Customer data (from queryset on views.py) and serializes into json format
    Author: Educated Camels
    """
    class Meta:
        model = Customer
        fields = ('url', 'first_name', 'last_name', 'created')


class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=User
         fields=('email','password') 


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Product data (from queryset on views.py) and serializes into json format
    Author: Bri Wyatt
    """
    class Meta:
        model = Product
        fields = ('url', 'price', 'title', 'product_type', 'description', 'customer', 'created')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Product Type data (from queryset on views.py) and serializes into json format
    Author: Dara Thomas
    """
    class Meta:
        model = ProductType
        exclude = ()


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Payment Type data (from queryset on views.py) and serializes into json format
    Author: Harry Epstein
    """
    class Meta:
        model = PaymentType
        fields = ('url', 'account_number', 'customer')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Purpose: Takes database query for Order data (from queryset on views.py) and serializes into json format
    Author: Miriam Rozenbaum
    """
    class Meta:
        model = Order
        fields = ('url', 'payment_type', 'customer', 'created')


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Author: Steve Brownlee
    """
    class Meta:
        model = OrderProduct
        fields = ('order', 'product', )


class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Author: Steve Brownlee
    """
    class Meta:
        model = OrderProduct
        fields = ('product', )
        depth = 1
