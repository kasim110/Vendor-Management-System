"""
URL configuration for vendor_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vendor import views as order_view
from purchase_orders import views as purchaseorder_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/vendors/', include('vendor.urls',namespace='vendors')),
    # path('api/purchase_orders/', include('purchase_orders.urls',namespace='purchase_orders')),




    path('api/vendors/', order_view.VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', order_view.VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/',order_view.VendorPerformanceAPIView.as_view(),name='vendor-performance'),

    path("api/purchase_orders/",purchaseorder_view.PurchaseOrderListCreateAPIView.as_view(),name="purchaseorder-list-create"),
    path("api/purchase_orders/<int:pk>/",purchaseorder_view.PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),name="purchaseorder-retrieve-update-destroy"),
    path('api/purchase_orders/<int:po_id>/acknowledge/',purchaseorder_view.AcknowledgePurchaseOrderAPIView.as_view(),name="acknowledge"),

]
