from django.contrib import admin
from django import forms
from purchase_orders.models import PurchaseOrderModel

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrderModel
        fields = '__all__'

    items = forms.JSONField(widget=forms.Textarea)

class PurchaseOrderAdmin(admin.ModelAdmin):
    form = PurchaseOrderForm

admin.site.register(PurchaseOrderModel, PurchaseOrderAdmin)
