from rest_framework import serializers
from vendor.models import VendorModel


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = '__all__'