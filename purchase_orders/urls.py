from django.urls import path,include
from purchase_orders import views


app_name = "purchase_orders"

urlpatterns = [ 
    path("",views.PurchaseOrderListCreateAPIView.as_view(),name="purchaseorder-list-create"),
    path("<int:pk>",views.PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),name="purchaseorder-retrieve-update-destroy"),
    path('/<int:po_id>/acknowledge/',views.AcknowledgePurchaseOrderAPIView.as_view(),name="acknowledge")


]