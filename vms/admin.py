from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.VendorModel)
admin.site.register(models.PurchaseOrderModel)
admin.site.register(models.PerformanceModel)