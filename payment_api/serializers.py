# from rest_framework import serializers
# from .models import Method, Payment

# class MethodSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
    
#     class Meta:
#         model = Method
#         fields = ['id', 'name']

#     def create(self, data):
#         return Method.objects.create(**data)

# class PaymentCreateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     method_id = serializers.PrimaryKeyRelatedField(queryset=Method.objects.all(), source='method', write_only=True)
    
#     class Meta:
#         model = Payment
#         fields = ['id', 'method_id', 'amount']

# class PaymentListSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     method = MethodSerializer(read_only=True)
#     date = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Payment
#         fields = ['id', 'method', 'date', 'amount']

#     def get_date(self, obj):
#         return obj.date.strftime('%d-%m-%Y %H:%M')
    










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