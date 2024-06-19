from rest_framework import serializers
from .models import CustomUser, Reservation

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'date_joined']

    def create(self, validated_data):
        password = validated_data.pop('password', None)  
        user = CustomUser.objects.create(**validated_data)
        if password is not None:
            user.set_password(password)  
            user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        password = validated_data.get('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'method', 'payment', 'date', 'time', 'number_of_guests', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.method = validated_data.get('method', instance.method)
        instance.payment = validated_data.get('payment', instance.payment)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.number_of_guests = validated_data.get('number_of_guests', instance.number_of_guests)
        instance.save()
        return instance
        