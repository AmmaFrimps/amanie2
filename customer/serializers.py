from rest_framework import serializers

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "area",
            "street",
            "zone",
            "house_no",
            "service_type",
            "rate",
        )


class PaymentRecordSerializer(serializers.ModelSerializer):
    #customer = CustomerSerializer()

    class Meta:
        model = PaymentRecord
        fields = (
            "customer",
            "payment_period",
            "amount_paid",
            "payment_type",
            "collector",
            "date_of_payment",
            "remarks",
        )


class BinSerializer(serializers.ModelSerializer):
    #customer = CustomerSerializer()

    class Meta:
        model = Bin
        fields = (
            'customer',
            'bin_id',
            'level',
            'code'
        )
