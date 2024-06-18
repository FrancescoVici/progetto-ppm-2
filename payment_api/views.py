from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Method, Payment
from .serializers import MethodSerializer, PaymentCreateSerializer, PaymentListSerializer

@api_view(['GET'])
def method_list(request):
    methods = Method.objects.all()
    serializer = MethodSerializer(methods, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_method(request):
    serializer = MethodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        # Simulate payment processing
        payment_status, transaction_id = self.process_payment(payment)
        payment.status = payment_status
        payment.transaction_id = transaction_id
        payment.save()

    def process_payment(self, payment):
        # Simulate integration with a payment gateway
        import random
        transaction_id = f'tx_{random.randint(100000, 999999)}'
        # Simulate success or failure
        if random.choice([True, False]):
            return 'completed', transaction_id
        else:
            return 'failed', transaction_id

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
