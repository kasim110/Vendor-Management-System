from django.shortcuts import render
from vendor.models import VendorModel
from rest_framework import generics,views,status
from .serializers import VendorListSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from purchase_orders.utils import update_on_time_delivery_rate, update_quality_rating_average, update_average_response_time, update_fulfillment_rate


class VendorListCreateAPIView(generics.ListAPIView,generics.CreateAPIView):

    queryset = VendorModel.objects.all()
    serializer_class = VendorListSerializer

    def get_serializer_context(self):
        return {
            "request":self.request,
            "args" : self.args,
            "kwargs" : self.kwargs
        }

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView,generics.DestroyAPIView,generics.ListAPIView,generics.UpdateAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VendorPerformanceAPIView(views.APIView):
    def get(self, request, vendor_id):
        vendor = get_object_or_404(VendorModel, pk=vendor_id)
        update_on_time_delivery_rate(vendor)
        update_quality_rating_average(vendor)
        update_average_response_time(vendor)
        update_fulfillment_rate(vendor)
        data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate
        }
        response_data = {"success": True,"data": data}
        return Response(response_data,status=status.HTTP_200_OK)