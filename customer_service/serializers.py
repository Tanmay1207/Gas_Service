from rest_framework import serializers
from .models import ServiceRequest, CustomerAccount
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ServiceRequestSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)

    class Meta:
        model = ServiceRequest
        fields = '__all__'
        read_only_fields = ['status', 'created_at', 'updated_at', 'resolved_at']

class CustomerAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CustomerAccount
        fields = '__all__'

