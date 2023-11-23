from django.shortcuts import render
from .models import PurchaseOrderModel,VendorModel,PerformanceModel
from .serializers import PurchaseOrderSerializer , VendorSerializer , PerformanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics,status
from django.db.models import Sum, Avg


# Create your views here.


class VendorGetCreate(generics.ListCreateAPIView):
    queryset=VendorModel.objects.all()
    serializer_class=VendorSerializer
  
  
class VendorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = VendorSerializer
    queryset = VendorModel.objects.all()
    
    

class PurchaseOrderGetCreate(generics.ListCreateAPIView):
    queryset=PurchaseOrderModel.objects.all()
    serializer_class=PurchaseOrderSerializer
  
  
class PurchaseOrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrderModel.objects.all()
    

    
@api_view(['GET'])
def performanceDetails(request,vendor_id):
    
    on_time_delivery_rate = PerformanceModel.objects.aggregate(average=Avg('on_time_delivery_rate'))
    quality_rating_avg = PerformanceModel.objects.aggregate(average=Avg('quality_rating_avg'))
    average_response_time = PerformanceModel.objects.aggregate(average=Avg('average_response_time'))
    fulfillment_rate = PerformanceModel.objects.aggregate(average=Avg('fulfillment_rate'))

    
    if request.method == 'GET':
        obj = VendorModel.objects.get(id=vendor_id)
        obj.on_time_delivery_rate = on_time_delivery_rate['average']
        obj.quality_rating_avg = quality_rating_avg['average']
        obj.average_response_time = average_response_time['average']
        obj.fulfillment_rate = fulfillment_rate['average']
        obj.save()
        
        obj1 = VendorModel.objects.get(id=vendor_id)
        serializer=PerformanceSerializer(obj1)
        return Response(serializer.data)