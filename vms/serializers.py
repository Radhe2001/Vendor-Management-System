from rest_framework import serializers
from .models import VendorModel,PerformanceModel,PurchaseOrderModel


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorModel
        fields="__all__"


class PerformanceSerializer(serializers.ModelSerializer):
    vendor=VendorSerializer(many=True,read_only=True)
    class Meta:
        model=PerformanceModel
        fields="__all__"



class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor=VendorSerializer(many=True,read_only=True)
    class Meta:
        model=PurchaseOrderModel
        fields="__all__"


