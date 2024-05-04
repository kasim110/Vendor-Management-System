from django.db.models import Count, Avg
from purchase_orders.models import PurchaseOrderModel
from django.utils import timezone

def update_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed')
    on_time_delivered_orders = completed_orders.filter(delivery_date__lte=timezone.now())
    total_completed_orders = completed_orders.count()
    if total_completed_orders > 0:
        on_time_delivery_rate = on_time_delivered_orders.count() / total_completed_orders
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.save()

def update_quality_rating_average(vendor):
    completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    if completed_orders.exists():
        quality_rating_avg = completed_orders.aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        vendor.quality_rating_avg = quality_rating_avg
        vendor.save()

def update_average_response_time(vendor):
    acknowledged_orders = PurchaseOrderModel.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    if acknowledged_orders.exists():
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() for order in acknowledged_orders]
        average_response_time = sum(response_times) / len(response_times)
        vendor.average_response_time = average_response_time
        vendor.save()
    else:
        vendor.average_response_time = 0  # No acknowledged orders, set to 0
        vendor.save()

def update_fulfillment_rate(vendor):
    total_orders = PurchaseOrderModel.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed').count()
    if total_orders > 0:
        fulfillment_rate = fulfilled_orders / total_orders
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()