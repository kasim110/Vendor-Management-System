from django.urls import path,include
from vendor import views


app_name = "vendors"

urlpatterns = [ 
    path('', views.VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('<int:pk>/', views.VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('<int:vendor_id>/performance/',views.VendorPerformanceAPIView.as_view(),name='vendor-performance')


]