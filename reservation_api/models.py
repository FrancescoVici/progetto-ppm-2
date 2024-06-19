from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    method = models.ForeignKey('payment_api.Method', on_delete=models.SET_NULL, null=True, blank=True) 
    payment = models.ForeignKey('payment_api.Payment', on_delete=models.SET_NULL, null=True, blank=True) 
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reservation {self.id} - {self.user.username} - {self.date}'
