from django.db import models
from datetime import datetime

# Create your models here.
class VendorModel(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField(default=100)
    quality_rating_avg = models.FloatField(default=100)
    average_response_time = models.FloatField(default=100)
    fulfillment_rate = models.FloatField(default=100)
    
    def __str__(self):
        return self.name
    
    

class PurchaseOrderModel(models.Model):
    po_number = models.CharField(max_length=100,unique=True)
    vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.now)
    delivery_date = models.DateTimeField(blank=True)
    items = models.JSONField()
    quality = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField(blank=True)
    acknowledgement_date = models.DateTimeField(blank=True)
    
    
    def __str__(self):
        return self.po_number
    
    
    
class PerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    date =  models.DateTimeField(blank=True)
    on_time_delivery_rate = models.FloatField(default=100)
    quality_rating_avg = models.FloatField(default=100)
    average_response_time = models.FloatField(default=100)
    fulfillment_rate = models.FloatField(default=100)
    
    
    def __str__(self):
        return str(self.vendor)
    