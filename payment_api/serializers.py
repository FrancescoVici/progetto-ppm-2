from rest_framework import serializers
from .models import Method, Payment

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = '__all__'

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['method', 'amount']

class PaymentListSerializer(serializers.ModelSerializer):
    method = MethodSerializer()

    class Meta:
        model = Payment
        fields = '__all__'