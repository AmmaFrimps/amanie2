from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Customer, PaymentRecord, Bin
from .serializers import CustomerSerializer, PaymentRecordSerializer, BinSerializer


# API Views
class CustomerCreateAndList(generics.ListCreateAPIView):
    search_fields = ['first_name', 'middle_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Customer.objects.all()


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)


# API Views
class PaymentRecordCreateAndList(generics.ListCreateAPIView):
    search_fields = ['first_name', 'middle_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PaymentRecordSerializer
    permission_classes = (IsAuthenticated,IsAdminUser)
    queryset = PaymentRecord.objects.all()


class PaymentRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentRecordSerializer
    permission_classes = (IsAuthenticated,IsAdminUser)


# API Views
class BinCreateAndList(generics.ListCreateAPIView):
    search_fields = ['first_name', 'middle_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BinSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Bin.objects.all()


class BinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    permission_classes = (IsAuthenticated,)

