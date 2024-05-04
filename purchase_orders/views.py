from django.shortcuts import render
from purchase_orders.models import PurchaseOrderModel
from rest_framework import generics,views
from .serializers import PurchaseOrderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from vendor.models import VendorModel
from purchase_orders.utils import  update_average_response_time


class PurchaseOrderListCreateAPIView(generics.ListAPIView,generics.CreateAPIView):

    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_serializer_context(self):
        return {
            "request":self.request,
            "args" : self.args,
            "kwargs" : self.kwargs
        }

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView,generics.DestroyAPIView,generics.ListAPIView,generics.UpdateAPIView):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class AcknowledgePurchaseOrderAPIView(views.APIView):
    def post(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrderModel, pk=po_id)
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        vendor = purchase_order.vendor
        update_average_response_time(vendor)
        return Response({'message': 'Purchase order acknowledged successfully'})