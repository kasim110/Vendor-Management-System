from django.db import models


class VendorModel(models.Model):
    name = models.CharField(max_length=105)
    contant_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50,unique=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)

    class  Meta:
        verbose_name = 'Vendor Details'
        verbose_name_plural = 'Vendor Details'

    def __str__(self) -> str:
        return f'{self.name}'
