from django.db import models
from vendor.models import VendorModel

class PurchaseOrderModel(models.Model):
    STATUS_CHOICE = (
        ("pending","Pending"),
        ("completed","Completed"),
        ("cancelled","Cancelled"),
    )
    po_number = models.CharField(max_length=255,unique=True)
    vendor = models.ForeignKey(VendorModel,on_delete=models.DO_NOTHING,related_name="purchaseorder_vendor")
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE,default='Pending')
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.po_number}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"