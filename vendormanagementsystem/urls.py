from django.contrib import admin
from django.urls import path
from vms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/',views.VendorGetCreate.as_view(),name="NewVendor"),
    path('api/vendors/<int:pk>/',views.VendorUpdateDelete.as_view(),name="ExistingVendor"),
    path('api/purchase_orders/',views.PurchaseOrderGetCreate.as_view(),name="NewOrder"),
    path('api/purchase_orders/<int:pk>/',views.PurchaseOrderUpdateDelete.as_view(),name="ExistingOrder"),
    path('api/vendors/<int:vendor_id>/performance/',views.performanceDetails,name="performance")
]
